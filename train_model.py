import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

# Load processed data
df = pd.read_csv("processed_sales.csv")

# Features and target
features = [
    'day', 'month', 'weekday', 'is_weekend',
    'lag_1', 'rolling_mean_7'
]

X = df[features]
y = df['sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Model
model = XGBRegressor(n_estimators=100, learning_rate=0.1)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("MAE:", mae)