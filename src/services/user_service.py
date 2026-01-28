import logging
from typing import List
from src.domain.models import User
from src.data.user_repository import UserRepository

logger = logging.getLogger(__name__)

class UserService:
    """Service layer for user-related business logic."""

    def __init__(self, user_repository: UserRepository = None):
        self.user_repository = user_repository or UserRepository()

    def fetch_all_users(self) -> List[User]:
        try:
            users = self.user_repository.get_all_users()
            logger.info(f"Fetched {len(users)} users from repository.")
            return users
        except Exception as e:
            logger.error(f"Error fetching users: {e}")
            raise