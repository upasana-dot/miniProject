from flask import Blueprint, jsonify,request
user_bp = Blueprint("users", __name__)
from database import get_connection

auth_bp = Blueprint("auth", __name__)

users={
    "admin":"1234"
}

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # conn = get_connection()
    # cursor = conn.cursor()

    # cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
    #                (username, password))
    # user = cursor.fetchone()
    # conn.close()

    # if user:
    #     return jsonify({"message": "Login successful"})
    # else:
    #     return jsonify({"message": "Invalid credentials"}), 401

    if users.get(username) == password:
        return jsonify({
            "message": "Login successful",
            "token": "dummy_token_123"
        })
    else:
        return jsonify({
            "message": "Invalid credentials"
        }), 401

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify({"message": "Users route working"})
