import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load processed data
df = pd.read_csv("processed_sales.csv")

# Features and target
features = [
    "day", "month", "weekday", "is_weekend",
    "lag_1", "rolling_mean_7"
]

X = df[features]
y = df["sales"]

# Train-test split (time-series safe → no shuffle)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# ✅ Improved model (more stable + reproducible)
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("✅ Model trained successfully!")
print(f"📊 MAE: {mae:.2f}")

# Save model
model_path = "model.pkl"
joblib.dump(model, model_path)

print(f"💾 Model saved at: {os.path.abspath(model_path)}")