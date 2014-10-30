from flask import Blueprint, render_template
from flask_login import current_user

from ..ext import google_login

pages = Blueprint("pages", __name__)


@pages.route("/")
def index():
    if current_user.is_authenticated():
        name = current_user.name
    else:
        name = None
    google_login_url = google_login.authorization_url()
    return render_template(
        "index.html",
        name=name,
        google_login_url=google_login_url,
    )
