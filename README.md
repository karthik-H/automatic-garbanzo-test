# JSONPlaceholder User Fetcher

A production-ready Python application that retrieves user data from the JSONPlaceholder API using Clean Architecture principles.

## Features

- Fetches all users from [JSONPlaceholder](https://jsonplaceholder.typicode.com/users)
- Clean, modular, and testable codebase
- Environment-based configuration
- Robust error handling and logging

## Project Structure

```
src/
  config/           # Configuration and environment loader
  data/             # Repository layer (API communication)
  domain/           # Domain models
  services/         # Business logic
  main.py           # Application entrypoint
```

## Setup

1. **Clone the repository**

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   The `.env` file is already provided:
   ```
   API_BASE_URL=https://jsonplaceholder.typicode.com
   ```

## Running the Application

```bash
python src/main.py
```

## Output

- The program will fetch and display all user records from the API.
- Any errors (e.g., network issues) will be logged and reported.

## Linting

This project follows [PEP8](https://peps.python.org/pep-0008/) standards. You can lint the code using:

```bash
pip install flake8
flake8 src/
```

## Notes

- No authentication is required for the JSONPlaceholder API.
- Only GET requests are performed.
- All configuration is managed via `.env` and environment variables.
