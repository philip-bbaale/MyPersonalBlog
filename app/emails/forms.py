from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class subscription_form(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Email()])
     submit = SubmitField('Subscribe')