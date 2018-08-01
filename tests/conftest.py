def pytest_configure():
    from django.conf import settings
    settings.configure(
        URLS_EXCLUDED_FROM_SIGNATURE_CHECK=[],
        DIRECTORY_API_CLIENT_BASE_URL='https://api.com',
        DIRECTORY_API_CLIENT_API_KEY='test-api-key',
        DIRECTORY_API_CLIENT_SENDER_ID='test-sender-id',
        DIRECTORY_API_CLIENT_DEFAULT_TIMEOUT=5,
    )
