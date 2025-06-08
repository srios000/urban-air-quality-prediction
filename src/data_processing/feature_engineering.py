import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def safe_label_transform(series, label_encoder):
    mapping = dict(
        zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))
    )
    return series.map(mapping).fillna(-1).astype(int)


def base_feature_engineering(
    df, verbose=True, le_country=None, le_loc=None, le_cat=None, fit_encoder=True
):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    pollutant_cols = ["pm25", "pm10", "o3", "no2", "so2", "co"]
    for col in pollutant_cols:
        lower = df[col].quantile(0.01)
        upper = df[col].quantile(0.99)
        df[col] = df[col].clip(lower, upper)
    df["dayofweek"] = df["date"].dt.dayofweek
    df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)
    df["total_pollutants"] = df[pollutant_cols].sum(axis=1)
    df["pm25_pm10_ratio"] = np.where(df["pm10"] != 0, df["pm25"] / df["pm10"], 0)

    if fit_encoder or le_country is None:
        le_country = LabelEncoder().fit(df["country"])
    df["country_encoded"] = safe_label_transform(df["country"], le_country)

    if fit_encoder or le_loc is None:
        le_loc = LabelEncoder().fit(df["loc"])
    df["loc_encoded"] = safe_label_transform(df["loc"], le_loc)

    if fit_encoder or le_cat is None:
        le_cat = LabelEncoder().fit(df["aqi_category"])
    df["aqi_cat_encoded"] = safe_label_transform(df["aqi_category"], le_cat)

    df["target"] = df["aqi_cat_encoded"]

    return df, le_country, le_loc, le_cat
