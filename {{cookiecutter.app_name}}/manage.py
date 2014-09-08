from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.ext import db

app = create_app()
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
