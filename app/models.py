from app import db


class Egg(db.Model):
    __tablename__ = 'eggs'
    id = db.Column(db.Integer, primary_key=True)
    date_collected = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now())
    color = db.Column(db.Integer, db.ForeignKey(
        'egg_colors.id'), nullable=False)
    weight = db.Column(db.Float)
    notes = db.Column(db.String(255))

    def __repr__(self):
        return f'<Egg: id={self.id}>'


class EggColor(db.Model):
    __tablename__ = 'egg_colors'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    egg_colors = db.relationship('Egg', backref='egg_colors', lazy=True)
    hens = db.relationship('Hen', backref='hens', lazy=True)

    def __repr__(self):
        return f'<EggColor: id={self.id}>'


class Hen(db.Model):
    __tablename__ = 'hens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    egg_color = db.Column(db.Integer, db.ForeignKey('egg_colors.id'))
    date_hatched = db.Column(db.Date, nullable=False)
    est_hatch = db.Column(db.Boolean, nullable=False)
    date_acquired = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Hen: name={self.name}>'
