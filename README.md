# directory-api-client
[Export Directory API client](https://www.directory.exportingisgreat.gov.uk/)

## Build status

[![CircleCI](https://circleci.com/gh/uktrade/directory-api-client/tree/master.svg?style=svg)](https://circleci.com/gh/uktrade/directory-api-client/tree/master)

## Requirements

## Installation

```shell
pip install git+https://github.com/uktrade/directory-api-client.git
```

## Usage

```python
from exportdirectory.client import DirectoryAPIClient

export_directory_client = DirectoryAPIClient(
    base_url="https://api.directory.exportingisgreat.gov.uk",
    api_key=api_key
)
```

### Send registration form

```python
export_directory_client.registration.send_form(
    form_data=form_data
)
```

### Confirm registration email

```python
notifications_client.confirm_email(
    confirmation_code=confirmation_code,
)
```

## Development

    $ git clone https://github.com/uktrade/directory-api-client
    $ cd directory-ui
    $ make
