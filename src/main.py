import logging
from src.services.user_service import UserService

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

def display_users(users):
    for user in users:
        print(f"ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Phone: {user.phone}")
        print(f"Website: {user.website}")
        print(f"Address: {user.address.street}, {user.address.suite}, {user.address.city}, {user.address.zipcode}")
        print(f"Geo: {user.address.geo.lat}, {user.address.geo.lng}")
        print(f"Company: {user.company.name} - {user.company.catchPhrase} - {user.company.bs}")
        print("-" * 60)

def main():
    setup_logging()
    user_service = UserService()
    try:
        users = user_service.fetch_all_users()
        display_users(users)
    except Exception as e:
        logging.error(f"Failed to retrieve users: {e}")

if __name__ == "__main__":
    main()