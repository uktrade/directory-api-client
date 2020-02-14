# Changelog

## [21.2.2](https://pypi.org/project/directory-api-client/21.2.2/) (2020-02-14)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/108/files)
- fix expose exportplan client

## [21.2.1](https://pypi.org/project/directory-api-client/21.2.1/) (2020-02-13)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/104/files)
- Add personalisation accessor to client

## [21.2.0](https://pypi.org/project/directory-api-client/21.2.0/) (2020-02-12)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/104/files)
- Add user location create handler

## [21.1.0](https://pypi.org/project/directory-api-client/21.1.0/) (2020-02-11)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/103/files)
- add export plan saving and retrieving 

## [21.0.0](https://pypi.org/project/directory-api-client/21.0.0/) (2019-10-02)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/102/files)
-- Add Name to be saved to supplier on collaborator_invite_accept

## [20.0.0](https://pypi.org/project/directory-api-client/20.0.0/) (2019-09-13)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/101/files)
## Fixed Bugs
- Added authentication to collaborator_create

## [19.0.0](https://pypi.org/project/directory-api-client/19.0.0/) (2019-09-09)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/101/files)

## Breaking changes
- `supplier.retrieve_profile` now expects sso_id rather than sso_session_id


## [18.0.0](https://pypi.org/project/directory-api-client/18.0.0/) (2019-09-03)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/99/files)

## Breaking changes
- Remove `sso_session_id` from call signature of `company.collaborator_invite_retrieve`

## [17.1.0](https://pypi.org/project/directory-api-client/17.1.0/) (2019-08-30)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/98/files)

## Implemented enhancements
- added method `company.collaborator_invite_delete`
- added method `company.collaborator_role_update`


## [17.0.0](https://pypi.org/project/directory-api-client/17.0.0/) (2019-08-29)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/97/files)

## Implemented enhancements
- added method `collaborator_invite_list`

## Breaking changes
The following methods on `company` have been renamed for consistency:

| old name                         | new name                      |
| -------------------------------- | ----------------------------- |
| update_profile                   | profile_update                |
| retrieve_private_profile         | profile_retrieve              |
| retrieve_public_profile          | published_profile_retrieve    |
| create_case_study                | case_study_create             |
| update_case_study                | case_study_update             |
| delete_case_study                | case_study_delete             |
| retrieve_private_case_study      | case_study_retrieve           |
| retrieve_public_case_study       | published_case_study_retrieve |
| request_collaboration            | collaborator_request_create   |
| remove_collaborators             | collaborator_disconnect       |
| add_collaborator                 | collaborator_create           |
| retrieve_collaborators           | collaborator_list             |
| create_transfer_invite           | collaborator_invite_create    |
| retrieve_transfer_invite         | collaborator_invite_retrieve  |
| accept_transfer_invite           | collaborator_invite_accept    |
| create_collaboration_invite      | collaborator_invite_create    |
| retrieve_collaboration_invite    | collaborator_invite_retrieve  |
| accept_collaboration_invite      | collaborator_invite_accept    |

## [16.3.0](https://pypi.org/project/directory-api-client/16.3.0/) (2019-08-28)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/96/files)
- Add handler for listing supplier sso ids

## [16.2.0](https://pypi.org/project/directory-api-client/16.2.0/) (2019-08-21)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/95/files)

## Implemented enhancements
- Add a new method to remove self from company profile

## [16.1.0](https://pypi.org/project/directory-api-client/16.1.0/) (2019-08-20)
[Full Changelog](https://github.com/uktrade/directory-api-client/pull/94/files)

## Implemented enhancements
- Add a new method to register second user to company profile

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
