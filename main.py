from flask import Flask, make_response, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired
from markupsafe import escape

import logic as lg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'The Hardest Secret key on The Planet'

class NameForm(FlaskForm):
    name = StringField('',validators=[DataRequired()])

def get_santa(Name):
    person = Name.upper()
    santa = lg.santa(person)
    return santa

@app.route('/', methods=['GET', 'POST'])
def root():
    form = NameForm()
    res = ' '
    if form.validate_on_submit():
        key = request.form.get('name').strip()
        if key is not None:
            res = get_santa(key)
    return render_template('index.html', form=form,Name=res)



