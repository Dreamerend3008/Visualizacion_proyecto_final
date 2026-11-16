from functools import reduce
from pathlib import Path

import pandas as pd


# Units documented by XM. UPME columns already contain GWh in their names.
XM_ENERGY_FILES = {
    "aportes_hidricos.csv",
    "demanda_comercial_reg.csv",
    "demanda_real_sin.csv",
    "generacion_real.csv",
    "media_historica_aportes.csv",
    "volumen_util_energia_embalse.csv",
    "volumen_util_energia_sistema.csv",
}
SEASON_MONTH = {
    "DJF": 1, "JFM": 2, "FMA": 3, "MAM": 4, "AMJ": 5, "MJJ": 6,
    "JJA": 7, "JAS": 8, "ASO": 9, "SON": 10, "OND": 11, "NDJ": 12,
}
# These detailed tables have a separate country/system-level table.
COUNTRY_REPLACED = {
    "upme_proyeccion_areas_mensual.csv",
    "volumen_util_energia_embalse.csv",
}
DATE_PARTS = {"YR", "anio", "mes"}


def _frequency(dates: pd.Series) -> str:
    unique = dates.drop_duplicates()
    if unique.dt.to_period("M").nunique() < len(unique):
        return "daily"
    if unique.dt.to_period("Y").nunique() == len(unique):
        return "yearly"
    return "monthly"


def _average(data: pd.DataFrame, date_column: str, period: str) -> pd.DataFrame:
    data[date_column] = data[date_column].dt.to_period(period).dt.to_timestamp()
    numbers = data.select_dtypes(include="number").columns.tolist()
    groups = [column for column in data.columns if column not in numbers]
    return data.groupby(groups, dropna=False, sort=False)[numbers].mean().reset_index()[data.columns]


def _collapse_hours(data: pd.DataFrame) -> pd.DataFrame:
    hours = [column for column in data if column.startswith("Values_Hour")]
    if hours:
        first = data.columns.get_loc(hours[0])
        data.insert(first, "Value", data[hours].mean(axis=1))
        data = data.drop(columns=hours)
    return data


def _add_oni_date(data: pd.DataFrame) -> pd.DataFrame:
    seasons = data["SEAS"].str.strip()
    unknown = set(seasons) - SEASON_MONTH.keys()
    if unknown:
        raise ValueError(f"Unknown CPC seasons: {sorted(unknown)}")
    data["SEAS"] = seasons
    data.insert(0, "fecha", pd.to_datetime({
        "year": data["YR"], "month": seasons.map(SEASON_MONTH), "day": 1,
    }))
    return data


def _country_parameters(data: pd.DataFrame, date_column: str, source: Path) -> pd.DataFrame | None:
    if source.name in COUNTRY_REPLACED:
        return None
    parameters = [
        column for column in data.select_dtypes(include="number").columns
        if column not in DATE_PARTS
    ]
    if not parameters:
        return None
    country = data.groupby(date_column, as_index=False)[parameters].mean()
    return country.rename(columns={
        column: f"{source.stem}__{column}" for column in parameters
    })


def _merge(frames: list[pd.DataFrame], date_column: str) -> pd.DataFrame:
    return reduce(
        lambda left, right: left.merge(right, on=date_column, how="outer"), frames
    ).sort_values(date_column).reset_index(drop=True)


def cleaning(raw_dir="data/raw", output_dir="data/clean") -> list[Path]:
    """Clean the raw CSVs and create country-level monthly and yearly tables."""
    raw_dir, output_dir = Path(raw_dir), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    written, monthly_parts, yearly_parts = [], [], []

    for source in sorted(raw_dir.glob("*.csv")):
        data = _collapse_hours(pd.read_csv(source))
        frequency = None

        if source.name in {"cpc_oni_historico.csv", "cpc_roni_historico.csv"}:
            data, date_column, frequency = _add_oni_date(data), "fecha", "monthly"
        else:
            date_column = next((c for c in ("Date", "fecha") if c in data), None)
            if date_column:
                data[date_column] = pd.to_datetime(data[date_column], errors="raise")
                frequency = _frequency(data[date_column])
                if frequency == "daily":
                    data = _average(data, date_column, "M")
                    frequency = "monthly"
                elif frequency == "monthly":
                    data[date_column] = data[date_column].dt.to_period("M").dt.to_timestamp()
                else:
                    data[date_column] = data[date_column].dt.to_period("Y").dt.to_timestamp()
            else:
                data = data.drop_duplicates()  # Reference data, not a time series.

        if source.name in XM_ENERGY_FILES:
            energy_columns = [column for column in data if column == "Value"]
            data[energy_columns] = data[energy_columns].div(1_000_000)
            data = data.rename(columns={column: f"{column}_GWh" for column in energy_columns})

        if date_column:
            summary = _country_parameters(data, date_column, source)
            if summary is not None:
                if frequency == "monthly":
                    summary = summary.rename(columns={date_column: "month"})
                    monthly_parts.append(summary)
                else:
                    summary = summary.rename(columns={date_column: "year"})
                    yearly_parts.append(summary)
            data[date_column] = data[date_column].dt.strftime("%Y-%m-%d")

        destination = output_dir / source.name
        data.to_csv(destination, index=False)
        written.append(destination)

    monthly = _merge(monthly_parts, "month")
    monthly["month"] = monthly["month"].dt.strftime("%Y-%m")
    monthly_path = output_dir / "all_parameters_monthly.csv"
    monthly.to_csv(monthly_path, index=False)

    yearly_from_monthly = monthly.copy()
    yearly_from_monthly["year"] = yearly_from_monthly.pop("month").str[:4].astype(int)
    yearly_from_monthly = yearly_from_monthly.groupby("year", as_index=False).mean()
    if yearly_parts:
        direct = _merge(yearly_parts, "year")
        direct["year"] = direct["year"].dt.year
        yearly_from_monthly = yearly_from_monthly.merge(direct, on="year", how="outer")
    yearly_path = output_dir / "all_parameters_yearly.csv"
    yearly_from_monthly.sort_values("year").to_csv(yearly_path, index=False)

    return written + [monthly_path, yearly_path]


if __name__ == "__main__":
    for path in cleaning():
        print(path)
