import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# --- Feature Engineering ---

# Basic time features
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['weekday'] = df['date'].dt.weekday

# Weekend flag
df['is_weekend'] = df['weekday'].apply(lambda x: 1 if x >= 5 else 0)

# Lag feature (previous day sales)
df['lag_1'] = df.groupby(['store_id', 'product_id'])['sales'].shift(1)

# Rolling average (last 7 days)
df['rolling_mean_7'] = df.groupby(['store_id', 'product_id'])['sales'].shift(1).rolling(7).mean()

# Drop missing values (from lag/rolling)
df.dropna(inplace=True)

# Save processed data
df.to_csv("processed_sales.csv", index=False)

print("Data pipeline completed! Processed file created.")