from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired
from utils.forms import MUltipleCheckboxField


class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    summary = TextAreaField()
    content = TextAreaField(validators=[DataRequired()])
    slug = StringField(validators=[DataRequired()])
    categories = MUltipleCheckboxField(coerce=int)


class CategoryForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    slug = StringField(validators=[DataRequired()])
    description = TextAreaField()


class SearchForm(FlaskForm):
    search_query = StringField(validators=[DataRequired()])