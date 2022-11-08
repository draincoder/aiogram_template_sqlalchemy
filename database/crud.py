import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import and_

from typing import List, Dict

from .models import *

logger = logging.getLogger(__name__)


class Database:

    def __init__(self, db_session: AsyncSession):
        self.session: AsyncSession = db_session

    async def add_user(self, user_id: int):
        async with self.session() as session:
            user: User = await session.get(User, user_id)
            if not user:
                session.add(User(user_id=user_id))
                await session.commit()
