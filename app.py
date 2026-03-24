from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

# Define input schema
class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    try:
        input_array = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_array)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}