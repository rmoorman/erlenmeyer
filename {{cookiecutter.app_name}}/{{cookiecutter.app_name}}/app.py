import os

from flask import Flask
from sassutils.wsgi import SassMiddleware

from . import ext, login, views
from .api import api


def create_app(**config):
    app = Flask(__name__)

    # Default config
    app.config.update(
        DEBUG=os.environ["DEBUG"],
        SECRET_KEY=os.environ["SECRET_KEY"],
        SQLALCHEMY_DATABASE_URI="postgresql://root:{}@db/{}".format(
            os.environ["MYSQL_ROOT_PASSWORD"],
            os.environ["MYSQL_DATABASE"],
        ),
        CSRF_ENABLED=True,
        GOOGLE_LOGIN_CLIENT_ID=os.environ.get("GOOGLE_LOGIN_CLIENT_ID"),
        GOOGLE_LOGIN_CLIENT_SECRET=os.environ.get("GOOGLE_LOGIN_CLIENT_SECRET"),
        GOOGLE_LOGIN_REDIRECT_SCHEME="http",
    )

    # Passed in config
    app.config.update(**config)

    # Extensions
    ext.db.init_app(app)
    ext.login_manager.init_app(app)
    ext.google_login.init_app(app)

    # Login
    login.setup(ext.login_manager)
    login.oauth2.setup(ext.google_login)

    # Views
    app.register_blueprint(views.pages)

    # API
    api.init_app(app)
    api.app = app

    # SASS
    if app.debug:
        app.wsgi_app = SassMiddleware(app.wsgi_app, dict(
            {{cookiecutter.app_name}}=("static/sass", "static/css", "/static/css"),
        ))

    return app
