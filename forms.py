from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email("Enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email("Enter Email:")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Sign In")

class Gear(Form):
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Go!') 
