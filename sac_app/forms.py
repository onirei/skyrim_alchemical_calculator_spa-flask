from flask_wtf import Form
from wtforms import SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired
from sac_app.models import Positive, Negative


#наполнение списка выборов для формы из бд
def selectors():
    select = [('', '',), ]
    positive = Positive.query.all()
    for _ in positive:
        select += [(_.attribute, _.attribute,), ]
    negative = Negative.query.all()
    for _ in negative:
        select += [(_.attribute, _.attribute,), ]
    return select


class CalculateForm(Form):
    attrib_1 = SelectField('', choices=selectors())
    attrib_2 = SelectField('', choices=selectors())
    attrib_3 = SelectField('', choices=selectors())
    attrib_4 = SelectField('', choices=selectors())

    choice_field = RadioField('Режим', choices=[('0', 'Поиск',), ('1', 'Оптимизация',)], default='0')
    choice_field_last = RadioField('Ключевой эффект', choices=[('0', 'Положительные',), ('1', 'Отрицательные',)], default='0')
    submit = SubmitField('Calculate')