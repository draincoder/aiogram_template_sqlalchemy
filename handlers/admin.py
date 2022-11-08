from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

from database.crud import Database
from filters.chat import PrivateChat


async def admin_start(message: Message, db: Database):
    await db.add_user(message.from_user.id)
    await message.answer('Hello, admin')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, PrivateChat(), CommandStart(), state="*", is_admin=False
    )
