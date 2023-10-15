from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired
# from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import EggColor


def choice_query():
    return EggColor.query


class EggLogForm(FlaskForm):
    color = SelectField('color', choices=[(
        1, 'brown-speckled'), (2, 'beige'), (3, 'brown')],  validators=[DataRequired()])
    # color = QuerySelectField(query_factory=choice_query,
    #                          allow_blank=False, get_label='color')
    weight = DecimalField('weight', places=1)
    submit = SubmitField('Submit')
