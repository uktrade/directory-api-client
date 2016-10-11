from hashlib import sha256
import json
import logging
import urllib.parse as urlparse

from monotonic import monotonic
import requests

from exportdirectory.version import __version__


logger = logging.getLogger(__name__)


class BaseAPIClient:
    def __init__(self, base_url=None, api_key=None):

        assert base_url, "Missing base url"
        assert api_key, "Missing API key"
        self.base_url = base_url
        self.api_key = api_key

    def put(self, url, data):
        return self.request("PUT", url, data=data)

    def get(self, url, params=None):
        return self.request("GET", url, params=params)

    def post(self, url, data):
        return self.request("POST", url, data=data)

    def delete(self, url, data=None):
        return self.request("DELETE", url, data=data)

    def request(self, method, url, data=None, params=None):

        logger.debug("API request {} {}".format(method, url))

        payload = json.dumps(data)

        headers = {
            "Content-type": "application/json",
            "User-agent": "EXPORT-DIRECTORY-API-CLIENT/{}".format(__version__),
        }

        url = urlparse.urljoin(self.base_url, url)

        start_time = monotonic()

        try:
            response = self.send(
                api_key=self.api_key,
                method=method,
                url=url,
                headers=headers,
                data=payload,
                params=params
            )
            if not response.ok:
                logger.error(
                    "API {} request on {} failed with {} '{}'".format(
                        method,
                        url,
                        response.status_code,
                        response.response
                    )
                )
                response.raise_for_status()
        finally:
            elapsed_time = monotonic() - start_time
            logger.debug(
                "API {} request on {} finished in {}".format(
                    method, url, elapsed_time
                )
            )

    def sign_request(self, api_key, url, prepared_request):
        url = urlparse.urlsplit(url)
        path = bytes(url.path, "utf-8")

        if url.query:
            path += bytes("?{}".format(url.query), "utf-8")

        salt = bytes(api_key, "utf-8")
        body = prepared_request.body or b""

        if isinstance(body, str):
            body = bytes(body, "utf-8")

        signature = sha256(path + body + salt).hexdigest()
        prepared_request.headers["X-Signature"] = signature

        return prepared_request

    def send(
            self, api_key, method, url, request=None, *args, **kwargs):

        prepared_request = requests.Request(
            method, url, *args, **kwargs
        ).prepare()

        signed_request = self.sign_request(
            api_key=api_key,
            url=url,
            prepared_request=prepared_request,
        )

        return requests.Session().send(signed_request)
