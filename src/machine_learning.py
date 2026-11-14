
"""
Machine Learning module
5G Printed Antenna Optimization
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def prepare_data(data):
    """Separate input features and target variables."""
    X = data[["Wp", "Lp", "Hs"]]
    y = data[["S11", "Gain"]]
    return X, y


def train_model(X, y):
    """Train a baseline Random Forest model."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)
    return model, X_test, y_test


if __name__ == "__main__":
    print("Machine Learning module initialized.")
