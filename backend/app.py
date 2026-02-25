from flask import Flask
from config import Config
from extensions import db
from routes.user_routes import user_bp
from dotenv import load_dotenv
load_dotenv()
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    db.init_app(app)
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app

app = create_app()

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def server_error(error):
    return {"error": "Internal server error"}, 500

if __name__ == "__main__":
    app.run(debug=True)
