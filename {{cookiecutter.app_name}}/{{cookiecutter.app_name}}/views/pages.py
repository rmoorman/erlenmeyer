from flask import Blueprint, render_template

pages = Blueprint("pages", __name__)


@pages.route("/")
def index():
    return render_template("index.html")
