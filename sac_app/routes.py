from sac_app import app
from sac_app.forms import CalculateForm
from sac_app.calculate import finder, optimizer
from flask import render_template, flash, redirect, url_for, jsonify, request




@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CalculateForm()
    if form.validate_on_submit():
        # определяем набор элементов
        if form.choice_field_last.data == '0':
            bd_data = 'Positive'
        else:
            bd_data = 'Negative'
        # определяем режим выборки
        if form.choice_field.data == '0':
            data = finder(form.attrib_1.data, form.attrib_2.data, form.attrib_3.data, form.attrib_4.data)
        else:
            data = optimizer(form.attrib_1.data, form.attrib_2.data, form.attrib_3.data, form.attrib_4.data, bd_data)
        return render_template('index.html', form=form, data=data)
    return render_template('index.html', form=form)
