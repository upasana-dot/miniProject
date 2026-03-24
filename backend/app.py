from flask import Flask, render_template,request, redirect, url_for
from models.predict import  predict_product_sales
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.user_model import db, User
import datetime
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"] = "sanchayAI_inventory_2026_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://upasanaporwal@localhost/upasanaporwal"
db.init_app(app)



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





# Routes ==========
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login",methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username").lower().strip()
        password = request.form.get("password").strip()

        print("Entered:", username, password)

        if not username or not password:
            return "Missing fields"

        username = username.lower().strip()
        password = password.strip()

    # simple authentication example
        user = User.query.filter_by(username=username).first()

        print("User from DB:", user)

        if user:
            print("DB password:", user.password)

        if user and user.password == password:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password"
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").lower().strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()

        if not username or not email or not password:
            return "All fields required"

        user = User(
            username=username,
            email=email,
            password=password
        )

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "User already exists"
        
        user = User(username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("login.html")


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
@login_required
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
        sales_data=sales_data,
        user= current_user,
        username=current_user.username
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
    inventory_data=get_inventory()
    return render_template("inventory.html",inventory=inventory_data)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/create_test_user")
def create_test_user():
    user = User(username="shivam", email="shivam@gmail.com", password="shivam123")
    db.session.add(user)
    db.session.commit()
    return "User created"


@app.route("/show_users")
def show_users():
    users = User.query.all()
    for u in users:
        print(u.username, u.password)
    return "Check terminal for users"

if __name__ == "__main__":
    app.run(debug=True, port=5002)