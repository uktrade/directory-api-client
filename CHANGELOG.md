# Changelog

## [16.0.0](https://pypi.org/project/directory-api-client/16.0.0/) (2019-08-16)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/92/files)

### Implemented enhancements
- Support Django 1.11.23 through 3.x
- Added request identity verification handler
- Removed use of TestCase with pytest

### Breaking changes
- Dropped support form Django <1.11.23
- Removed company.list_public_profiles

## [15.1.0](https://pypi.org/project/directory-api-client/15.1.0/) (2019-07-04)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/91/files)

### Implemented enhancements
- Support Django 1.11.22 through 2.x

## [15.0.0](https://pypi.org/project/directory-api-client/15.0.0/) (2019-07-04)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/90/files)

### Implemented enhancements
- Use fallback cache on more endpoints that support it

### Bugs fixed
- Removed fallback cache usage for endpoints can leak user details

### Breaking changes
- Removed `company.search_case_study`
- Renamed `company.search_company` to `company.search_find_a_supplier`

## [14.0.1](https://pypi.org/project/directory-api-client/14.0.1/) (2019-07-04)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/88/files)

### Implemented enhancements
- No ticket - Can now import the instantiated client as `from directory_api_client import api_client`
- No ticket - Remove `version.py`

### Bugs fixed
- No ticket - Upgrade vulnerable django version to django 1.11.22

## [14.0.0](https://pypi.org/project/directory-api-client/14.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/87/files)

**Implemented enhancements:**

- Upgraded directory client core to reduce overzealous logging from the fallback cache.
- Improved documentation in readme.
- The client responses are now subclasses of `request.Response`.

**Breaking changes:**

- Directory client core has been upgraded a major version 5.0.0. [See](https://github.com/uktrade/directory-client-core/pull/16)
- Dropped support for Python 3.5
- The client responses dropped the `raw_response` property. The attributes of `raw_response` are now available on the client responses.
