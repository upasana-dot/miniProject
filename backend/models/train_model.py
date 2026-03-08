# import pandas as pd
# import pickle
# import os
# from sklearn.linear_model import LinearRegression
# import datetime

# # Absolute path handling
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_PATH = os.path.join(BASE_DIR, "/Users/upasanaporwal/Desktop/project/backend/data/sales_data_sample.csv")
# MODEL_PATH = os.path.join(BASE_DIR, "saved_model.pkl")

# # Load dataset
# df = pd.read_csv(
#     "/Users/upasanaporwal/Desktop/project/backend/data/sales_data_sample.csv",
#     encoding="latin1"
# )

# df.columns = df.columns.str.strip().str.lower()
# print("Columns:",df.columns)

# df["orderdate"] = pd.to_datetime(df["orderdate"])
# df["month"] = df["orderdate"].dt.month
# df["year"]= df["orderdate"].dt.year

# monthly_sales=df.groupby(["year","month"])["quantityordered"].sum().reset_index()

# X = monthly_sales[["year","month"]]
# y = monthly_sales["quantityordered"]

# model = LinearRegression()
# model.fit(X, y)

# # Save model inside models folder
# with open(MODEL_PATH, "wb") as f:
#     pickle.dump(model, f)

# print("✅ Model trained and saved successfully!")



import pandas as pd
import sqlite3
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# connect database
# conn = sqlite3.connect("sales_data_sample.csv")
# query = """
# SELECT PRODUCTCODE, YEAR_ID, MONTH_ID, SALES
# FROM sales_data
# """

df = pd.read_csv("/Users/upasanaporwal/Desktop/project/backend/data/sales_data_sample.csv",encoding="latin1")

# convert productcode to numeric
encoder = LabelEncoder()
df["PRODUCTCODE"] = encoder.fit_transform(df["PRODUCTCODE"])

# features and target
X = df[["PRODUCTCODE","MONTH_ID","YEAR_ID"]]
y = df["SALES"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# random forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

# save model
pickle.dump(model,open("models/saved_model.pkl","wb"))

# save label encoder
pickle.dump(encoder,open("models/product_encoder.pkl","wb"))

print("Random Forest Model trained successfully")