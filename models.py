from manage import db
from sqlalchemy import inspect

def dictify(object, exclude=[]):
    mapper = inspect(type(object))

    return {
        column.key: getattr(object, column.key) for column in mapper.attrs if column.key not in exclude
    }

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    atx = db.Column(db.String(length=128), nullable=True)
    title = db.Column(db.String(length=256), nullable=True)
    filtered_title = db.Column(db.String(length=256), nullable=True)

    href = db.Column(db.String(length=256), nullable=True)

    owner = db.Column(db.String(length=256), nullable=True)
    distributer = db.Column(db.String(length=256), nullable=True)
    conditions = db.Column(db.Text, nullable=True)
    mkb_codes = db.Column(db.Text, nullable=True)
    mkb_testimony = db.Column(db.Text, nullable=True)
    extra = db.Column(db.Text, nullable=True)
    active_substance = db.Column(db.Text, nullable=True)
    forms = db.Column(db.Text, nullable=True)
    composition = db.Column(db.Text, nullable=True)
    clphgroup = db.Column(db.Text, nullable=True)
    phthgroup = db.Column(db.Text, nullable=True)
    indication = db.Column(db.Text, nullable=True)
    influence = db.Column(db.Text, nullable=True)
    kinetics = db.Column(db.Text, nullable=True)
    dosage = db.Column(db.Text, nullable=True)
    side_effects = db.Column(db.Text, nullable=True)
    preg_lact = db.Column(db.Text, nullable=True)

    hepato = db.Column(db.Text, nullable=True)
    contra = db.Column(db.Text, nullable=True)
    renal = db.Column(db.Text, nullable=True)
    child = db.Column(db.Text, nullable=True)
    old = db.Column(db.Text, nullable=True)
    special = db.Column(db.Text, nullable=True)
    over_dosage = db.Column(db.Text, nullable=True)
    interaction = db.Column(db.Text, nullable=True)
    pharm = db.Column(db.Text, nullable=True)
    anons = db.Column(db.Text, nullable=True)

    def as_dict(self):
        return dictify(self)

