from sklearn.model_selection import train_test_split


def split(X_tree, y, mask):
    X_tree_filtered = X_tree[mask]
    y_filtered = y[mask]

    # Tree model split
    X_tree_train, X_tree_temp, y_tree_train, y_temp_tree = train_test_split(
        X_tree_filtered, y_filtered, test_size=0.4, random_state=42, stratify=y_filtered
    )

    X_tree_val, X_tree_test, y_tree_val, y_tree_test = train_test_split(
        X_tree_temp, y_temp_tree, test_size=0.5, random_state=42, stratify=y_temp_tree
    )

    return (
        X_tree_train,
        X_tree_val,
        X_tree_test,
        y_tree_train,
        y_tree_val,
        y_tree_test,
    )


def split_classic(X_tree, y, mask):
    X_tree_filtered = X_tree[mask]
    y_filtered = y[mask]

    # Tree model split
    X_tree_train, X_tree_val, y_tree_train, y_tree_val = train_test_split(
        X_tree_filtered, y_filtered, test_size=0.2, random_state=42, stratify=y_filtered
    )

    return (
        X_tree_train,
        X_tree_val,
        y_tree_train,
        y_tree_val,
    )
