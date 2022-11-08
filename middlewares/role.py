from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from models.role import UserRole
from typing import List


class RoleMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, admin_ids: List[int]):
        super().__init__()
        self.admin_ids = admin_ids

    async def pre_process(self, obj, data, *args):
        if not getattr(obj, "from_user", None):
            data["role"] = None
        elif obj.from_user.id in self.admin_ids:
            data["role"] = UserRole.ADMIN
            print(1)
        else:
            data["role"] = UserRole.USER

    async def post_process(self, obj, data, *args):
        del data["role"]
