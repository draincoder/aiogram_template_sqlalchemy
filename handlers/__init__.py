from aiogram import Dispatcher

from .user import register_user
from .admin import register_admin


def register_handlers(dp: Dispatcher):
    register_admin(dp)
    register_user(dp)
