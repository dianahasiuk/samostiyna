from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, URL, Optional
from app.recipes.models import Category


class RecipeForm(FlaskForm):
    # Назва
    title = StringField(
        "Назва страви",
        validators=[DataRequired(), Length(max=200)]
    )

    # Короткий опис (для списку рецептів)
    short_description = TextAreaField(
        "Короткий опис",
        validators=[Optional(), Length(max=300)]
    )

    # Розширений опис
    description = TextAreaField(
        "Опис",
        validators=[Optional()]
    )

    # Фото
    image_url = StringField(
        "Фото (URL)",
        validators=[Optional(), URL(message="Введіть коректну URL-адресу")]
    )

    # Інгредієнти
    ingredients = TextAreaField(
        "Інгредієнти",
        validators=[Optional()]
    )

    # Кроки приготування
    steps = TextAreaField(
        "Кроки приготування",
        validators=[Optional()]
    )

    # Час
    cooking_time = IntegerField(
        "Час приготування (хв.)",
        validators=[Optional(), NumberRange(min=1, message="Мінімум 1 хвилина")]
    )

    # Категорія
    category_id = SelectField(
        "Категорія",
        coerce=int,
        validators=[Optional()]
    )

    # Кнопка
    submit = SubmitField("Зберегти")

    def set_category_choices(self):
        """Підтягує список категорій із бази."""
        self.category_id.choices = [
            (c.id, c.name)
            for c in Category.query.order_by(Category.name).all()
        ]
