import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from config import DATA_URL
import joblib


def load_data():
    df = pd.read_csv(DATA_URL)
    df = df[
        [
            "GDP per capita",
            "headcount_upper_mid_income_povline",
            "year",
            "Healthy Life Expectancy (IHME)",
        ]
    ].dropna()
    return df


def train_and_save_model():
    df = load_data()
    X = df[["GDP per capita", "headcount_upper_mid_income_povline", "year"]]
    y = df["Healthy Life Expectancy (IHME)"]

    model = RandomForestRegressor(random_state=42, n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, "rf_model.pkl")
    print("Модель збережена у rf_model.pkl")
    return model


def get_feature_importance(model):
    feature_names = ["GDP per capita", "headcount_upper_mid_income_povline", "year"]
    importances = model.feature_importances_
    return dict(zip(feature_names, importances))
