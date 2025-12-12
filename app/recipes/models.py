from datetime import datetime
from app.extensions import db
from flask_login import UserMixin

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    # Зв'язок з рецептами
    recipes = db.relationship("Recipe", backref="category", lazy=True)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    # Короткий опис (для превʼю)
    short_description = db.Column(db.String(300), nullable=True)

    # Повний опис
    description = db.Column(db.Text, nullable=True)

    # Фото (URL)
    image_url = db.Column(db.String(500), nullable=True)

    # Основні поля рецепта
    ingredients = db.Column(db.Text, nullable=True)
    steps = db.Column(db.Text, nullable=True)

    cooking_time = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Категорія
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    # Автор рецепта (дозволимо nullable=True щоб адміністратор міг додати тестові)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
