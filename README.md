## 🚀 Live Demo

- 🌐 Render: https://demand-forecasting-ml-adet.onrender.com/docs
- ☁️ AWS EC2: http://18.118.147.166:8000/docs

## 🧠 Overview

This project predicts product demand using machine learning with time-series feature engineering (lag features, rolling averages).

## ⚙️ Tech Stack

- Python
- Scikit-learn (RandomForest)
- FastAPI
- AWS EC2
- Render

## 📊 Model Performance
- Mean Absolute Error (MAE): ~4.6

## ▶️ How to Run

```bash
pip install pandas numpy scikit-learn xgboost fastapi uvicorn joblib
python generate_data.py
python data_pipeline.py
python train_model.py
uvicorn main:app --reload
