from flask import Flask, render_template,request, redirect, url_for
from models.predict import  predict_product_sales
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.user_model import  User
from werkzeug.security import generate_password_hash, check_password_hash
from models.product import Product
import datetime
import pandas as pd
import os
import json
from extensions import db
from authlib.integrations.flask_client import OAuth
from flask_wtf import CSRFProtect


# flash("Invalid username or password", "error")

app = Flask(__name__)
app.config["SECRET_KEY"] =   "sanchayAI_inventory_2026_secret_key"  # os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://upasanaporwal@localhost/upasanaporwal"
app.config['SESSION_COOKIE_HTTPONLY']= True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()



def get_product_codes():
    df = pd.read_csv("data/sales_data_sample.csv",encoding="latin1")   # change path if needed
    products = df["PRODUCTCODE"].unique()
    return products.tolist()


def get_inventory():
    df = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")
    inventory = df.groupby("PRODUCTCODE").agg({
        "QUANTITYORDERED":"sum",
        "SALES":"sum"
    }).reset_index()

    inventory.rename(columns={
        "PRODUCTCODE":"product",
        "QUANTITYORDERED":"stock",
        "SALES":"sales"
    }, inplace=True)

    inventory["status"] = inventory["stock"].apply(
        lambda x: "Low Stock" if x < 200 else "Available"
    )
    return inventory.to_dict(orient="records")




login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()


@app.before_request
def check_csrf():
    print("FORM DATA:", request.form)



# Routes ==========
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login",methods=["GET","POST"])
def login():
    print("Route hit")

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")


        print("Entered:", email, password)
        # print("User from DB:",user)

        if email:
            email=email.strip().lower()
        if password:
            password=password.strip()

        # if not email:
        #     flash("Email is required")
        #     return redirect(url_for("login")+"?mode=login")

        if not email or not password:
            return "Missing fields"
            return redirect(url_for("login"))

    # simple authentication example
        user = User.query.filter_by(email=email).first()

        if user:
           print("Stored hash:", user.password)

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/dashboard")
        else:
            flash("Invalid email or password")
            return redirect(url_for("login")+"?mode=login")
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
@csrf.exempt
def register():
    if request.method == "POST":
        username = request.form.get("username").lower().strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()

        if not username or not email or not password:
            flash( "All fields required")
            return redirect("/register")
        
        if "@" not in email:
            flash("Invalid email")
            return redirect("/register")
        
        if len(password) <6:
            flash("Password must be at least 6 characters")
            return redirect("/register")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("User already exists")
            return redirect("/register")
        
        hashed_password = generate_password_hash(password)

        user=User(
            username=username,
            email=email,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please log in.")
        return redirect(url_for("login")+"?mode=login")
    
    return redirect(url_for("login"))



@app.route("/admin")
@login_required
def admin():
    if current_user.role != "admin":
        return "Access Denied"
    return "Admin Panel"


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/dashboard",methods=["GET","POST"])
@csrf.exempt
@login_required
def dashboard():
    products=get_product_codes()

    prediction=None
    selected_product=None
    sales_data=[]
    # prediction_graph={"actual": [],"predicted":[]}

    total_products=len(products)
    inventory=get_inventory()

    low_stock=sum(1 for item in inventory if item["status"] == "Low Stock")
    critical=sum(1 for item in inventory if item["status"] == "Critical")

    accuracy = get_model_accuracy()

    accuracy_data = {
        "labels": ["Model Accuracy"],
        "values": [accuracy]
    }

    # prediction_graph=get_prediction_graph()
    prediction_graph={"actual":[],"predicted":[]}
   
    if request.method=="POST":
        product_code = request.form["product_code"]
        month = request.form.get("month")
        year = request.form.get("year")

        # prediction=predict_product_sales(product_code,month,year)

        
        if not product_code or not  month or not  year:
            flash("All fields required")
            return redirect("/dashboard")
        
        try:
            month=int(month)
            year=int(year)
        except:
            flash("Invalid month or year")
            return redirect("/dashboard")
        
        if not (1 <= month <= 12):
            flash("Invalid month")
            return redirect("/dashboard")

        if not (2020 <= year <= 2030):
            flash("Invalid year")
            return redirect("/dashboard")


        selected_product=product_code

        prediction = predict_product_sales(product_code, month, year)

        prediction_graph={
            "actual":[],
            "predicted":[prediction]
        }
        prediction_graph={
            "actual":[],
            "predicted":[prediction]
        }
        sales_data=[
                {
                    "product": product_code, 
                    "label":f"{month}/{year}",
                    "sales": prediction
                }]
        print("FINAL GRAPH :"   , prediction_graph)
        prediction_graph = get_prediction_graph()        

    return render_template("dashboard.html",
        products=products,
        prediction=prediction,
        selected_product=selected_product,
        sales_data=sales_data,
        prediction_graph=prediction_graph,
        user= current_user,
        username=current_user.username,
        total_products=total_products,
        low_stock=low_stock,
        critical=critical,
        accuracy=accuracy,
        accuracy_data=accuracy_data
    )

def get_model_accuracy():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(BASE_DIR, "models/model_accuracy.txt")

        with open(path, "r") as f:
            return round(float(f.read()) * 100, 2)
    except:
        return 0.0
    
def get_prediction_graph():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join("models/prediction_data.json")
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {"actual": [], "predicted": []}


@app.route("/forecast", methods=["GET","POST"])
@csrf.exempt
@login_required
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
    inventory_data=get_inventory()
    return render_template("inventory.html",inventory=inventory_data)
def get_inventory():
    df = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")

    inventory = df.groupby("PRODUCTCODE").agg({
        "QUANTITYORDERED":"sum",
        "SALES":"sum"
    }).reset_index()

    inventory.rename(columns={
        "PRODUCTCODE":"product",
        "QUANTITYORDERED":"stock",
        "SALES":"sales"
    }, inplace=True)

    # 🔥 ALERT LOGIC
    def get_status(x):
        if x < 100:
            return "Critical"
        elif x < 200:
            return "Low Stock"
        else:
            return "Available"

    inventory["status"] = inventory["stock"].apply(get_status)
    return inventory.to_dict(orient="records")

@app.route("/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    if request.method == "POST":
        product_code = request.form.get("product_code")
        product_name = request.form.get("product_name")
        stock = request.form.get("stock")

        if not product_code or not product_name or not stock:
            flash("All fields required")
            return redirect("/add-product")

        try:
            stock = int(stock)
        except:
            flash("Stock must be a number")
            return redirect("/add-product")

        # check duplicate
        existing = Product.query.filter_by(product_code=product_code).first()
        if existing:
            flash("Product already exists")
            return redirect("/add-product")

        new_product = Product(
            product_code=product_code,
            product_name=product_name,
            stock=stock
        )

        db.session.add(new_product)
        db.session.commit()

        flash("Product added successfully")
        return redirect("/dashboard")

    return render_template("add_product.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# show_users route
@app.route("/show_users")
def show_users():
    users = User.query.all()
    for u in users:
        print(u.username, u.password)
    return "Check terminal for users"


# delete route
@app.route("/delete_users")
def delete_users():
    User.query.delete()
    db.session.commit()
    return "All users deleted"


if __name__ == "__main__":
    app.run(debug=True, port=5005)