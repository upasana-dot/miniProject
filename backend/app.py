from flask import Flask, render_template,request, redirect, url_for
from models.predict import  predict_product_sales
import datetime
import pandas as pd


app = Flask(__name__)


def get_product_codes():
    df = pd.read_csv("data/sales_data_sample.csv",encoding="latin1")   # change path if needed
    products = df["PRODUCTCODE"].unique()
    return products.tolist()


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        Username = request.form["Username"]
        Password = request.form["Password"]
    # simple authentication example
        if Username == "admin" and Password == "1234":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password"
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    products=get_product_codes()
    prediction=None
    selected_product=None
    sales_data=[]
    if request.method=="POST":
        product_code = request.form["product_code"]
        month = request.form.get("month")
        year = request.form.get("year")

        if product_code and month and year:
            month = int(month)
            year = int(year)
            selected_product=product_code

            prediction=predict_product_sales(product_code,month,year)
            sales_data=[
                {
                    "product": product_code, 
                    "label":f"{month}/{year}",
                    "sales": prediction
                }]

    return render_template("dashboard.html",
        products=products,
        prediction=prediction,
        selected_product=selected_product,
        sales_data=sales_data
    )


@app.route("/forecast", methods=["GET","POST"])
def forecast():
    print("cgjyfjhgjg",request.method)

    products = get_product_codes()

    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]
    sales_data = []

    if request.method == "POST":
        print("wertghcg")
        product_code = request.form["product_code"]
        year = int(request.form["year"])

        print("selected product: ", product_code, "year:", year)
        for m in range(1,13):
            pred = predict_product_sales(product_code, m, year)
            print("Month:",m,"Prediction:",pred)
            sales_data.append(pred)

    return render_template(
        "forecast.html",
        products=products,
        months=months,
        sales_data=sales_data
    )

    
@app.route("/inventory")
def inventory():
    return render_template("inventory.html")


if __name__ == "__main__":
    app.run(debug=True)