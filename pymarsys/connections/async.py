# -*- coding: utf-8 -*-

import json
from urllib.parse import urljoin

import aiohttp

from .base import EMARSYS_URI, BaseConnection
from .exceptions import ApiCallError


class AsyncConnection(BaseConnection):
    """
    Asynchronous connection for Ermasys or inherited-from BaseEndpoint objects.
    """

    def __init__(self, username, secret, uri=EMARSYS_URI):
        super().__init__(username, secret, uri)
        self.session = aiohttp.ClientSession()

    async def make_call(self,
                        method,
                        endpoint,
                        headers=None,
                        payload=None,
                        params=None):
        """
        Make an authenticated asynchronous HTTP call to the Emarsys api using
        the aiohttp library.
        :param method: HTTP method.
        :param endpoint: Emarsys' api endpoint.
        :param headers: HTTP headers.
        :param payload: HTTP payload.
        :param params : HTTP params.
        :return: Coroutine with the result of the query.
        """
        if not payload:
            payload = {}

        if not params:
            params = {}

        url = urljoin(self.uri, endpoint)
        headers = self.build_headers(headers)
        async with self.session.request(
                method,
                url,
                headers=headers,
                data=json.dumps(payload),
                params=params
        ) as response:
            try:
                response.raise_for_status()
            except aiohttp.errors.HttpProcessingError as err:
                raise ApiCallError(
                    'Error message: "{}" \n Error details: "{}"'.format(
                        err,
                        await response.text()
                    )
                )
            return await response.json()
