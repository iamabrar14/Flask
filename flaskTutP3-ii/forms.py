from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length


class RegistrationForm(FlaskForm):
    name=StringField("Full Name : ",validators=[DataRequired(message="We need your email")])
    email=StringField("Email : ",validators=[DataRequired(message="Email is required"),Email(message="That is not a valid email")])
    password=PasswordField("Password : ",validators=[DataRequired(message="Password is required"),Length(min=6,message="Please enter at least 6 characters")])
    submit=SubmitField("Register")
    