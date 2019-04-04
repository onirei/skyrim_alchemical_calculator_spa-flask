from sac_app import app
from sac_app.forms import CalculateForm
from sac_app.calculate import finder, optimizer
from flask import render_template, jsonify, request


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

@app.route('/api', methods=['GET'])
def get():
    attrib_1 = request.args.get('attrib_1', default = '', type = str)
    attrib_2 = request.args.get('attrib_2', default='', type=str)
    attrib_3 = request.args.get('attrib_3', default='', type=str)
    attrib_4 = request.args.get('attrib_4', default='', type=str)
    mode = request.args.get('mode', default='', type=str)
    bd_data = request.args.get('bd_data', default='', type=str)
    data2 = []
    if mode == 'finder':
        data = finder(attrib_1, attrib_2, attrib_3, attrib_4)
        for _ in data:
            data2.append(_[0])
    elif mode == 'optimizer':
        data = optimizer(attrib_1, attrib_2.data, attrib_3, attrib_4, bd_data)
        for _ in data:
            data2.append(_[0])
    else:
        data2 = []
    return jsonify({'data': data2})