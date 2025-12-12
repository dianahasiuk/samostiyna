from flask import Flask, render_template
from app.extensions import db, migrate, login_manager


def create_app():
    app = Flask(__name__)

    # --------------------------
    # Налаштування конфігурації
    # --------------------------
    app.config['SECRET_KEY'] = "super-secret-key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --------------------------
    # Ініціалізація розширень
    # --------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # --------------------------
    # Імпорт моделей (ВАЖЛИВО!)
    # --------------------------
    from app import models
    from app.recipes import models as recipe_models

    # --------------------------
    # Реєстрація Blueprint-ів
    # --------------------------
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.recipes import recipes_bp
    app.register_blueprint(recipes_bp, url_prefix="/recipes")

    # --------------------------
    # Головна сторінка
    # --------------------------
    @app.route("/")
    def home():
        return render_template("home.html")

    return app
