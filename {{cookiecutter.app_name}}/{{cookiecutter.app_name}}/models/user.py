from flask_login import UserMixin
from simpleflake import simpleflake

from ..ext import db
from ..util import now


class User(db.Model, UserMixin):

    id = db.Column(db.String(255), default=simpleflake, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    secret = db.Column(db.String(255), nullable=True)
    google_id = db.Column(db.String(255), unique=True, nullable=True)

    created_at = db.Column(db.Integer, default=now, nullable=False)
