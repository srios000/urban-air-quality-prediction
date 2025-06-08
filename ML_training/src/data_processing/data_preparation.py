from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def prepare_for_tree_models(df_fe):
    cols_to_use = [
        "pm25",
        "pm10",
        "o3",
        "no2",
        "so2",
        "co",
        "dayofweek",
        "is_weekend",
        "total_pollutants",
        "pm25_pm10_ratio",
        "country_encoded",
        "loc_encoded",
    ]
    return df_fe[cols_to_use]


def prepare_for_linear_models(df_fe, preprocessor=None, fit=True):
    # Kolom kategorikal dan numerik
    categorical_cols = ["country", "loc"]
    numerical_cols = [
        "pm25",
        "pm10",
        "o3",
        "no2",
        "so2",
        "co",
        "total_pollutants",
        "pm25_pm10_ratio",
        "dayofweek",
        "is_weekend",
    ]

    # Drop kolom yang tidak digunakan
    df_cleaned = df_fe.drop(
        columns=[
            "aqi_category",
            "target",
            "country_encoded",
            "loc_encoded",
            "aqi_cat_encoded",
            "date",
        ]
    )

    if fit or preprocessor is None:
        preprocessor = ColumnTransformer(
            [
                ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
                ("num", StandardScaler(), numerical_cols),
            ]
        )
        X_processed = preprocessor.fit_transform(df_cleaned).toarray()
    else:
        X_processed = preprocessor.transform(df_cleaned)

    return X_processed, preprocessor
