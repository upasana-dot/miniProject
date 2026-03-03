# import pickle
# import numpy as np

# def predict_next_month(month_number):
#     with open("models/saved_model.pkl", "rb") as f:
#         model = pickle.load(f)

#     prediction = model.predict(np.array([[month_number]]))
#     return round(prediction[0], 2)

import pickle
import numpy as np
import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "saved_model.pkl")

def predict_next_month():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    today = datetime.datetime.now()
    next_month = today.month + 1
    year = today.year

    if next_month > 12:
        next_month = 1
        year += 1

    # VERY IMPORTANT → Pass both year and month
    prediction = model.predict(np.array([[year, next_month]]))

    return round(prediction[0], 2)