import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib


df = pd.read_csv("data/sales_data_sample.csv",encoding="latin1")
new_data=pd.read_csv("data/new_data.csv",encoding="latin1")

final_data=pd.concat([df,new_data])

# base path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df=final_data

# convert productcode to numeric
encoder = LabelEncoder()
df["PRODUCTCODE"] = encoder.fit_transform(df["PRODUCTCODE"])
df = df.dropna(subset=["SALES"])

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

# save paths
model_path = os.path.join(BASE_DIR, "saved_model.pkl")
encoder_path = os.path.join(BASE_DIR, "product_encoder.pkl")

# save
pickle.dump(model, open(model_path, "wb"))
pickle.dump(encoder, open(encoder_path, "wb"))


print(" Random Forest Model trained successfully")