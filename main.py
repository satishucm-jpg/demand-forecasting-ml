from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ✅ Define app FIRST
app = FastAPI(title="Demand Forecasting API")

# Load model
model = joblib.load("model.pkl")


# Input schema
class PredictionInput(BaseModel):
    day: int
    month: int
    weekday: int
    is_weekend: int
    lag_1: float
    rolling_mean_7: float

@app.post("/predict")
def predict(data: PredictionInput):
    try:
        input_df = pd.DataFrame([{
            "day": data.day,
            "month": data.month,
            "weekday": data.weekday,
            "is_weekend": data.is_weekend,
            "lag_1": data.lag_1,
            "rolling_mean_7": data.rolling_mean_7
        }])

        prediction = model.predict(input_df)

        return {"prediction": prediction.tolist()}

    except Exception as e:
        return {"error": str(e)}