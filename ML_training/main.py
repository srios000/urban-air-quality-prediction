import pandas as pd
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import pickle
from pathlib import Path

# local module
from src.data_processing.feature_engineering import base_feature_engineering
from src.data_processing.data_preparation import prepare_for_tree_models
from src.data_processing.data_split import split
from src.models.evaluation import cross_val
from src.models.tuning import random_search


def main():
    base_dir = Path(__file__).resolve().parent

    # Build path to the CSV
    data_path = (
        base_dir.parent
        / "ML_training"
        / "data"
        / "processed"
        / "air_quality_data_clean.csv"
    )

    # load dataset
    aqi_dataset = pd.read_csv(data_path)
    print("data loaded successfully !\n")

    # ==== Step 2: Persiapan data ====
    (aqi_dataset_fe, aqi_le_country, aqi_le_loc, aqi_le_cat) = base_feature_engineering(
        aqi_dataset
    )
    target = aqi_dataset_fe["target"]
    X_tree = prepare_for_tree_models(aqi_dataset_fe)

    # ==== Step 3: Split data 60% train, 20% val, 20% test ====
    class_counts = pd.Series(target).value_counts()
    classes_to_keep = class_counts[class_counts >= 2].index

    mask = pd.Series(target).isin(classes_to_keep)

    (X_train, X_val, X_test, y_train, y_val, y_test) = split(X_tree, target, mask)

    # Untuk tree model
    print(f"Train size (tree): {X_train.shape[0]}")
    print(f"Validation size (tree): {X_val.shape[0]}")
    print(f"Test size (tree): {X_test.shape[0]}\n")

    # ==== Step 4: Create Model ====
    model = XGBClassifier(eval_metric="mlogloss", random_state=42)
    model.fit(X_train, y_train)
    model_validation = model.predict(X_val)

    print("✅ XGBosst Classification Report:")
    print(classification_report(y_val, model_validation))
    print("-" * 60)

    # ==== Step 5: Model evaluations ====
    cross_val("XGBoost", model, X_train, y_train)

    # ==== Step 6: Model fine tune ====
    tuner = random_search(model, X_train, y_train)

    # Hasil parameter terbaik
    print("\n🔍 Best Parameters:", tuner.best_params_)
    # Model terbaik dari hasil tuning
    best_model = tuner.best_estimator_

    cross_val("Best XGBoost", best_model, X_train, y_train)

    # ==== Step 7: Save model to server dir ====
    # Get the absolute path to the current script (inference.py)
    base_dir = Path(__file__).resolve().parent

    # Construct the absolute path to the # Model directory (2 levels up, then into server/infrastructure/...)
    model_path = base_dir.parent / "server" / "infrastructure" / "ml" / "models_store"

    # Simpan encoder ke file
    with open(model_path / "le_country.pkl", "wb") as f:
        pickle.dump(aqi_le_country, f)

    with open(model_path / "le_loc.pkl", "wb") as f:
        pickle.dump(aqi_le_loc, f)

    with open(model_path / "le_cat.pkl", "wb") as f:
        pickle.dump(aqi_le_cat, f)
    # Simpan model XGBoost terbaik
    with open(model_path / "xgboost_final_model.pkl", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    main()
