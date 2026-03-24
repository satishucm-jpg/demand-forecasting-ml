import pandas as pd
import numpy as np

np.random.seed(42)

days = 365
stores = 3
products = 5

data = []

for store in range(1, stores + 1):
    for product in range(1, products + 1):
        base_demand = np.random.randint(50, 200)

        for day in range(days):
            date = pd.Timestamp("2023-01-01") + pd.Timedelta(days=day)

            weekly_pattern = 10 * np.sin(2 * np.pi * date.dayofweek / 7)
            trend = day * 0.1
            noise = np.random.normal(0, 5)

            sales = base_demand + weekly_pattern + trend + noise

            data.append([date, store, product, max(0, int(sales))])

df = pd.DataFrame(data, columns=["date", "store_id", "product_id", "sales"])

df.to_csv("sales.csv", index=False)

print("Dataset created!")