import requests_mock


def stub_request(url, http_method):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with requests_mock.mock() as mock:
                method = getattr(mock, http_method)
                method(url, text='')
                return func(*args, **kwargs)
        return wrapper
    return decorator
