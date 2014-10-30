from . import oauth2
from .. import models


def user_loader(user_id):
    return models.User.query.get(user_id)


def setup(login_manager):
    login_manager.user_loader(user_loader)
