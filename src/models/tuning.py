from sklearn.model_selection import RandomizedSearchCV


def random_search(model, X, y):
    # Parameter grid untuk tuning
    param_dist = {
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 5, 7, 10],
        "learning_rate": [0.01, 0.05, 0.1, 0.2],
        "subsample": [0.6, 0.8, 1.0],
        "colsample_bytree": [0.6, 0.8, 1.0],
    }
    # Randomized Search dengan 3-fold CV
    tuner = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_dist,
        n_iter=20,
        scoring="accuracy",
        cv=3,
        verbose=2,
        random_state=42,
        n_jobs=-1,
    )

    # Fit ke training set
    tuner.fit(X, y)

    return tuner
