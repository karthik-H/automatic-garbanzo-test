import pytest
from unittest.mock import patch, MagicMock
from src.main import main

# Test Case 1: test_successful_user_fetch_and_display
def test_successful_user_fetch_and_display():
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        mock_user_service = MagicMock()
        mock_user_service.fetch_all_users.return_value = users
        mock_user_service_cls.return_value = mock_user_service

        main()

        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_user_service.fetch_all_users.assert_called_once()
        mock_display_users.assert_called_once_with(users)
        mock_logging.error.assert_not_called()

# Test Case 2: test_successful_empty_user_list
def test_successful_empty_user_list():
    users = []
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        mock_user_service = MagicMock()
        mock_user_service.fetch_all_users.return_value = users
        mock_user_service_cls.return_value = mock_user_service

        main()

        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_user_service.fetch_all_users.assert_called_once()
        mock_display_users.assert_called_once_with(users)
        mock_logging.error.assert_not_called()

# Test Case 3: test_fetch_users_raises_exception
def test_fetch_users_raises_exception():
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        mock_user_service = MagicMock()
        mock_user_service.fetch_all_users.side_effect = Exception('Database unavailable')
        mock_user_service_cls.return_value = mock_user_service

        main()

        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_user_service.fetch_all_users.assert_called_once()
        mock_display_users.assert_not_called()
        mock_logging.error.assert_called_once_with('Failed to retrieve users: Database unavailable')

# Test Case 4: test_display_users_raises_exception
def test_display_users_raises_exception():
    users = [{'id': 1, 'name': 'Alice'}]
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users', side_effect=Exception('Display error')) as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        mock_user_service = MagicMock()
        mock_user_service.fetch_all_users.return_value = users
        mock_user_service_cls.return_value = mock_user_service

        main()

        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_user_service.fetch_all_users.assert_called_once()
        mock_display_users.assert_called_once_with(users)
        mock_logging.error.assert_called_once_with('Failed to retrieve users: Display error')

# Test Case 5: test_setup_logging_raises_exception
def test_setup_logging_raises_exception():
    with patch('src.main.setup_logging', side_effect=Exception('Logging setup failed')) as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        with pytest.raises(Exception) as excinfo:
            main()
        assert 'Logging setup failed' in str(excinfo.value)
        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_not_called()
        mock_display_users.assert_not_called()
        mock_logging.error.assert_not_called()

# Test Case 6: test_user_service_constructor_raises_exception
def test_user_service_constructor_raises_exception():
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService', side_effect=Exception('Init error')) as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        with pytest.raises(Exception) as excinfo:
            main()
        assert 'Init error' in str(excinfo.value)
        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_display_users.assert_not_called()
        mock_logging.error.assert_not_called()