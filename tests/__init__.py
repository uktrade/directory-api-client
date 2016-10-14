import requests_mock


def stub_request(url, http_method, expose=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with requests_mock.mock() as mock:
                mocked_method = getattr(mock, http_method)
                mocked_method(url, text='')
                args += (mock,)
                return func(*args, **kwargs)
        return wrapper
    return decorator
