from models import *
import re


def find_by_name(name: str) -> list:
    name = name.lower().strip()
    name = re.sub('[^а-яa-z0-9]', '', name)

    if name:
        return Medicine.query.filter(Medicine.filtered_title.like(name + '%')).all()

    return []


def find_by_atx(atx: str) -> list:
    atx = atx.upper().strip()

    return Medicine.query.filter(atx=atx).all()


def get_by_id(id: int):
    return Medicine.query.filter_by(id=id).first()
