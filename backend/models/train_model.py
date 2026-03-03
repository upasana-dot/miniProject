# import pandas as pd
# import pickle
# from sklearn.linear_model import LinearRegression

# # Load dataset
# df = pd.read_csv("data/sales_data.csv")

# # Convert date to numeric month index
# df["date"] = pd.to_datetime(df["date"])
# df["month"] = df["date"].dt.month

# # Features & Target
# X = df[["month"]]
# y = df["units_sold"]

# # Train model
# model = LinearRegression()
# model.fit(X, y)

# # Save model
# with open("models/saved_model.pkl", "wb") as f:
#     pickle.dump(model, f)

# print("Model trained and saved successfully!")


import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression
import datetime

# Absolute path handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "/Users/upasanaporwal/Desktop/project/backend/data/sales_data_sample.csv")
MODEL_PATH = os.path.join(BASE_DIR, "saved_model.pkl")

# Load dataset
df = pd.read_csv(
    "/Users/upasanaporwal/Desktop/project/backend/data/sales_data_sample.csv",
    encoding="latin1"
)

df.columns = df.columns.str.strip().str.lower()
print("Columns:",df.columns)

df["orderdate"] = pd.to_datetime(df["orderdate"])
df["month"] = df["orderdate"].dt.month
df["year"]= df["orderdate"].dt.year

monthly_sales=df.groupby(["year","month"])["quantityordered"].sum().reset_index()

X = monthly_sales[["year","month"]]
y = monthly_sales["quantityordered"]

model = LinearRegression()
model.fit(X, y)

# Save model inside models folder
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")