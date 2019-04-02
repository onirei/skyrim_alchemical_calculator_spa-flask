from flask_wtf import Form
from wtforms import SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired
import sqlite3

#наполнение списка выборов для формы из бд
def selectors():
    select = [('', '',),]
    conn = sqlite3.connect("sac_app/Skyrim.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM Positive")
    result = cursor.fetchall()
    conn.close()
    for i in range(len(result)):
        select += ((result[i][0], result[i][0],),)
    conn = sqlite3.connect("sac_app/Skyrim.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM Negative")
    result = cursor.fetchall()
    conn.close()
    for i in range(len(result)):
        select += [(result[i][0], result[i][0],),]
    return select


class CalculateForm(Form):
    attrib_1 = SelectField('', choices=selectors())
    attrib_2 = SelectField('', choices=selectors())
    attrib_3 = SelectField('', choices=selectors())
    attrib_4 = SelectField('', choices=selectors())

    choice_field = RadioField('Режим', choices=[('0', 'Поиск',), ('1', 'Оптимизация',)], default='0')
    choice_field_last = RadioField('Ключевой эффект', choices=[('0', 'Положительные',), ('1', 'Отрицательные',)], default='0')
    submit = SubmitField('Calculate')