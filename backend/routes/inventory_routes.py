from flask import Blueprint, jsonify
from services.inventory_service import get_inventory

inventory_bp = Blueprint("inventory", __name__)


inventory_data = [
    {"product": "Product A", "stock": 120, "reorder": 150},
    {"product": "Product B", "stock": 300, "reorder": 200}
]

@inventory_bp.route("/inventory")
def inventory():
    return jsonify(get_inventory())