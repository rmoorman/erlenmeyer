import os

from flask import Flask
from sassutils.wsgi import SassMiddleware

from . import ext, views
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
    )

    # Passed in config
    app.config.update(**config)

    # Extensions
    ext.db.init_app(app)
    ext.login_manager.init_app(app)

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
