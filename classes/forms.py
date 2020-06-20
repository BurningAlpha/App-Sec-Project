from wtforms import (
    BooleanField,
    Form,
    PasswordField,
    RadioField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import InputRequired, Email, Length


class LoginForm(Form):
    username = StringField("Username", [InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", [InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("Remember")


class RegisterForm(Form):
    email = StringField("Email", [InputRequired(), Email("Please enter your email address"), Length(max=120)])
    username = StringField("Username", [InputRequired(), Length(min=4, max=25)])
    password = PasswordField("Password", [InputRequired(), Length(min=8, max=80)])


class ReviewForm(Form):
    review_rating = SelectField("Review Rating", [InputRequired()], choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")], default="5", render_kw={"class": "form-control"})
    review_contents = TextAreaField("Review Contents", [Length(max=255)], render_kw={"class": "form-control"})
