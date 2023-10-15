from flask import render_template, redirect, url_for
from app import app, db
from app.forms import EggLogForm
from app.models import Egg
from sqlalchemy.sql import text


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    egg_count = db.session.execute(text(
        'SELECT YEAR( `date_collected` ), MONTH( `date_collected` ), COUNT( * ) FROM `eggs` GROUP BY YEAR( `date_collected` ), MONTH( `date_collected` )')).all()
    count_by_hen = db.session.execute(text(
        'SELECT `hens`.`name`, COUNT( `eggs`.`color` ) FROM `hens` LEFT JOIN `eggs` ON `hens`.`egg_color` = `eggs`.`color` GROUP BY `hens`.`name`')).all()
    form = EggLogForm()
    if form.validate_on_submit():
        egg = Egg(color=form.color.data, weight=form.weight.data)
        db.session.add(egg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Got an Egg', form=form, eggCount=egg_count, countByHen=count_by_hen)
