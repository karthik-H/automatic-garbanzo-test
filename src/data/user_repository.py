import requests
from typing import List
from src.domain.models import User, Address, AddressGeo, Company
from src.config.config import config


class UserRepository:
    """Repository for fetching user data from the JSONPlaceholder API."""

    def __init__(self, base_url: str = None):
        self.base_url = base_url or config.api_base_url

    def get_all_users(self) -> List[User]:
        url = f"{self.base_url}/users"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            users_json = response.json()
            return [self._parse_user(user) for user in users_json]
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch users: {e}")

    def _parse_user(self, data: dict) -> User:
        address_geo = AddressGeo(
            lat=data["address"]["geo"]["lat"],
            lng=data["address"]["geo"]["lng"]
        )
        address = Address(
            street=data["address"]["street"],
            suite=data["address"]["suite"],
            city=data["address"]["city"],
            zipcode=data["address"]["zipcode"],
            geo=address_geo
        )
        company = Company(
            name=data["company"]["name"],
            catchPhrase=data["company"]["catchPhrase"],
            bs=data["company"]["bs"]
        )
        return User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"],
            phone=data["phone"],
            website=data["website"],
            address=address,
            company=company
        )