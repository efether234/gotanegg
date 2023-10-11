from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import EggLogForm
from app.models import Egg
from sqlalchemy.sql import text

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    eggCount = db.session.execute(text('SELECT YEAR( `date_collected` ), MONTH( `date_collected` ), COUNT( * ) FROM `eggs` GROUP BY YEAR( `date_collected` ), MONTH( `date_collected` )')).all()
    form = EggLogForm()
    if form.validate_on_submit():
        egg = Egg(color=form.color.data)
        db.session.add(egg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Got an Egg', form=form, eggCount=eggCount)
