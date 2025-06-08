from sklearn.model_selection import cross_validate
from sklearn.metrics import (
    make_scorer,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)


def cross_val(name, model, X, y):
    # Skor yang ingin dievaluasi
    scoring = {
        "accuracy": "accuracy",
        "f1_macro": "f1_macro",
        "precision_macro": "precision_macro",
        "recall_macro": "recall_macro",
    }
    results = {}

    print("🔁 Cross-validation Results:\n")
    scores = cross_validate(model, X, y, cv=5, scoring=scoring, n_jobs=-1)
    results[name] = scores
    print(f"📌 {name}")
    for metric in scoring.keys():
        mean = scores[f"test_{metric}"].mean()
        std = scores[f"test_{metric}"].std()
        print(f"{metric:<15}: {mean:.4f} ± {std:.4f}")
    print("-" * 50)
