import pickle
import numpy as np
import os
import datetime
import joblib
import pandas as pd

# for random forest model with product code

model = pickle.load(open("models/saved_model.pkl","rb"))
encoder = pickle.load(open("models/product_encoder.pkl","rb"))

def predict_product_sales(product_code,month,year):
    product_encoded = encoder.transform([product_code])[0]

    data = pd.DataFrame(
        [[product_encoded, month, year]],
        columns=["PRODUCTCODE","MONTH_ID","YEAR_ID"]
    )

    prediction = model.predict([[product_encoded,month,year]])

    return round(float(prediction[0]),2)