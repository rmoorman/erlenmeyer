from flask import flash, redirect, url_for
from flask_login import login_user

from .. import models
from ..ext import db


def login_success(token, profile):
    user = models.User.query.filter_by(
        google_id=profile["id"],
    ).first()
    if not user:
        user = models.User.query.filter_by(
            email=profile["email"].lower(),
        ).first()
    if not user:
        user = models.User(
            name=profile["name"],
            email=profile["email"],
            google_id=profile["id"],
        )
        db.session.add(user)
        db.commit()
    login_user(user)
    return redirect(url_for("pages.index"))


def login_failure(e):
    flash(str(e))
    return redirect(url_for("pages.index"))


def setup(oauth2_login):
    oauth2_login.login_success(login_success)
    oauth2_login.login_failure(login_failure)

