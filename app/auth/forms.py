from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import User

class RegisterForm(FlaskForm):
    username = StringField("Логін", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Зареєструватися")

class LoginForm(FlaskForm):
    username = StringField("Логін", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Увійти")
