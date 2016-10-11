from contextlib import contextmanager
from unittest import mock


@contextmanager
def mock_requests():
    with mock.patch('requests.Session'):
        yield
