import pandas as pd
from prophet import Prophet

def run_forecast():
    df = pd.read_csv("data/sales.csv")
    df.columns = ["ds", "y"]

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    next_value = forecast["yhat"].iloc[-1]

    return {"next_month_prediction": int(next_value)}