from flask_login import LoginManager
from flask_oauth2_login import GoogleLogin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
google_login = GoogleLogin()
