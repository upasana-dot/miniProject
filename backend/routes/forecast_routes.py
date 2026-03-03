from flask import Blueprint, jsonify
from ml.prophet_model import run_forecast

forecast_bp = Blueprint("forecast", __name__)

@forecast_bp.route("/forecast", methods=["GET"])
def forecast():
    return jsonify({
        "next_month_prediction": 250
    })
    # return jsonify(run_forecast())