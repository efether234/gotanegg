from app import db

class Egg(db.Model):
    __tablename__ = 'eggs'
    id = db.Column(db.Integer, nullable=False,  primary_key=True)
    date_collected = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    color = db.Column(db.Integer, db.ForeignKey('egg_colors.id'), nullable=False)
    weight = db.Column(db.Float)
    notes = db.Column(db.String(255))

    def __repr__(self):
        return '<Egg: id={}>'.format(self.id)

class EggColor(db.Model):
    __tablename__ = 'egg_colors'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    egg_colors = db.relationship('Egg', backref='egg_colors', lazy=True)

    def __repr__(self):
        return '<EggColor: id={}>'.format(self.id)

