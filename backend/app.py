# from flask import Flask
# from flask_cors import CORS
# from flask import Blueprint , jsonify
# import sqlite3
# import logging


# from routes.dashboard_routes import dashboard_bp
# from routes.inventory_routes import inventory_bp
# from routes.forecast_routes import forecast_bp

# app = Flask(__name__)
# CORS(app)

# from routes.auth_routes import auth_bp
# app.register_blueprint(auth_bp)
# app.register_blueprint(dashboard_bp)
# app.register_blueprint(inventory_bp)
# app.register_blueprint(forecast_bp)

# @app.route("/")
# def home():
#     return {"message": "AI Supply Chain Backend Running"}

# if __name__ == "__main__":
#     app.run(debug=True, port=5002)

from flask import Flask, render_template
from models.predict import predict_next_month
import datetime

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():

    next_month = datetime.datetime.now().month + 1
    if next_month > 12:
        next_month = 1

    predicted_demand = predict_next_month()

    data = {
        "predicted_demand": f"{predicted_demand} units",
        "total_products": 120,
        "low_stock": 3,
        "inventory_cost": "₹2.4 Lakh",
        "inventory_summary": [
            {"product": "Product A", "stock": 120, "status": "Low"},
            {"product": "Product B", "stock": 300, "status": "Good"}
        ]

    }

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5006)