from flask_wtf import FlaskForm
from wtforms.fields import EmailField
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])



class RegisterForm(FlaskForm):
    username = StringField()
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])