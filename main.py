from flask import Flask, make_response, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

import logic as lg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'The Hardest Secret key on The Planet'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class NameForm(FlaskForm):
    name = StringField('Enter your Name: ',validators=[DataRequired()])
    # submit = SubmitField('Submit')

def get_santa(Name):
    ip = Name.upper()
    name = lg.santa(ip)
    print(name)
    return name

@app.route('/', methods=['GET', 'POST'])
def root():
    form = NameForm()
    res = 'SANTOSH SIR'
    if form.validate_on_submit():
        key = request.form.get('name')
        if key is not None:
            res = get_santa(key)
    return render_template('index.html', form=form,Name=res)

    
if __name__ == '__main__':
    db.create_all()


