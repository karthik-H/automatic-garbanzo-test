import pytest
from unittest.mock import patch, MagicMock, call
from src.main import main

# Test Case 1: Successful user fetch and display
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

# Test Case 2: Empty user list handling
def test_empty_user_list_handling():
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

# Test Case 3: Exception during user fetch
def test_exception_during_user_fetch():
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        mock_user_service = MagicMock()
        mock_user_service.fetch_all_users.side_effect = Exception('Database error')
        mock_user_service_cls.return_value = mock_user_service

        main()

        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_user_service.fetch_all_users.assert_called_once()
        mock_display_users.assert_not_called()
        mock_logging.error.assert_called_once_with('Failed to retrieve users: Database error')

# Test Case 4: Logging setup failure
def test_logging_setup_failure():
    with patch('src.main.setup_logging', side_effect=Exception('Logging configuration failed')) as mock_setup_logging, \
         patch('src.main.UserService') as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        with pytest.raises(Exception) as excinfo:
            main()
        assert 'Logging configuration failed' in str(excinfo.value)
        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_not_called()
        mock_display_users.assert_not_called()
        mock_logging.error.assert_not_called()

# Test Case 5: Exception during user display
def test_exception_during_user_display():
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

# Test Case 6: Large user list handling
def test_large_user_list_handling():
    users = [{'id': i, 'name': f'User{i}'} for i in range(10000)]
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

# Test Case 7: UserService instantiation failure
def test_userservice_instantiation_failure():
    with patch('src.main.setup_logging') as mock_setup_logging, \
         patch('src.main.UserService', side_effect=Exception('Init failed')) as mock_user_service_cls, \
         patch('src.main.display_users') as mock_display_users, \
         patch('src.main.logging') as mock_logging:

        with pytest.raises(Exception) as excinfo:
            main()
        assert 'Init failed' in str(excinfo.value)
        mock_setup_logging.assert_called_once()
        mock_user_service_cls.assert_called_once()
        mock_display_users.assert_not_called()
        mock_logging.error.assert_not_called()