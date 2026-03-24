# Demand Forecasting ML System

Built an end-to-end machine learning system to forecast product demand using time-series data.

## 🚀 Features
- Synthetic data generation simulating real-world sales patterns
- Feature engineering (lag features, rolling averages, seasonality)
- XGBoost regression model for demand prediction
- REST API using FastAPI for real-time predictions

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn, XGBoost
- FastAPI
- Docker (optional)

## 📊 Model Performance
- Mean Absolute Error (MAE): ~4.6

## ▶️ How to Run

```bash
pip install pandas numpy scikit-learn xgboost fastapi uvicorn joblib
python generate_data.py
python data_pipeline.py
python train_model.py
uvicorn main:app --reload
