from flask import Flask
from configs.app_config import AppConfig
from models.bank_model import db
from routes import routes

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(AppConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(routes)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)