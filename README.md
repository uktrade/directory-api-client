# directory-api-client
Export Directory internal API client.

## Build status

[![CircleCI](https://circleci.com/gh/uktrade/directory-api-client/tree/master.svg?style=svg)](https://circleci.com/gh/uktrade/directory-api-client/tree/master)

## Requirements

## Installation

```shell
pip install -e git+https://git@github.com/uktrade/directory-api-client.git@0.0.2#egg=directory-api-client
```

## Usage

```python
from directory_api_client.client import DirectoryAPIClient

directory_client = DirectoryAPIClient(
    base_url="https://api.directory.exportingisgreat.gov.uk",
    api_key=api_key
)
```

### Send registration form

```python
directory_client.registration.send_form(
    form_data=form_data
)
```

### Confirm registration email

```python
directory_client.registration.confirm_email(
    confirmation_code=confirmation_code,
)
```

## Development

    $ git clone https://github.com/uktrade/directory-api-client
    $ cd directory-ui
    $ make
