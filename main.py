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


@app.get("/")
def home():
    return {"message": "Demand Forecasting API is running!"}


@app.post("/predict")
def predict(data: PredictionInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)

    return {
        "predicted_sales": round(float(prediction[0]), 2)
    }