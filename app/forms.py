from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class EggLogForm(FlaskForm):
    color = SelectField('color', choices=[(1, 'brown'), (2, 'beige'), (3, 'brown-speckled')],  validators=[DataRequired()])
    submit = SubmitField('Submit')
