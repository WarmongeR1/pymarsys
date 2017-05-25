# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import requests

from .base import BaseConnection, EMARSYS_URI
from .exceptions import ApiCallError


class SyncConnection(BaseConnection):
    """
    Synchronous connection for Ermasys or inherited-from BaseEndpoint objects.
    """

    def __init__(self, username, secret, uri=EMARSYS_URI):
        super().__init__(username, secret, uri)

    def make_call(self,
                  method,
                  endpoint,
                  headers=None,
                  payload=None,
                  params=None):
        """
        Make an authenticated synchronous HTTP call to the Emarsys api using
        the requests library.
        :param method: HTTP method.
        :param endpoint: Emarsys' api endpoint.
        :param headers: HTTP headers.
        :param payload: HTTP payload.
        :param params: HTTP params.
        :return: Dictionary with the result of the query.
        """
        if not payload:
            payload = {}

        if not params:
            params = {}

        url = urljoin(self.uri, endpoint)
        headers = self.build_headers(headers)
        response = requests.request(
            method,
            url,
            headers=headers,
            json=payload,
            params=params
        )
        self.raise_errors_on_failure(response)
        self.raise_errors_on_limits(response)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise ApiCallError(
                'Error message: "{}" \n Error details: "{}"'.format(
                    err,
                    response.text
                )
            )
        return response.json()
