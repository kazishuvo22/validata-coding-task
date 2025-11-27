from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BankForm(FlaskForm):
    name = StringField("Bank Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Submit")
