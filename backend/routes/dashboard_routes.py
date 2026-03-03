from flask import Blueprint, jsonify

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def get_dashboard():
    return jsonify({
        "predicted_demand": "+18%",
        "total_products": 120,
        "low_stock": 3,
        "inventory_cost": "₹2.4 Lakh"
    })