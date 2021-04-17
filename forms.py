from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange


all_species = ["cat", "dog", "porcupine"]


class NewPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField('Species', choices=[(sp, sp) for sp in all_species])
    photo_url = StringField("Pet Photo URL", validators=[Optional(), URL(require_tld=True, message="Please provide a valid URL")])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(0,30, message="Age must be between 0 and 30.")])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Pet is Available")