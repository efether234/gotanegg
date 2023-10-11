from app import app, db
from app.models import Egg, EggColor

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Egg': Egg, 'EggColor': EggColor}
