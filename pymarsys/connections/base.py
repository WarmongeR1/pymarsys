# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import uuid
from abc import ABC, abstractmethod

__all__ = [
    'EMARSYS_URI',
    'BaseConnection',
]
EMARSYS_URI = 'https://api.emarsys.net/'


class BaseConnection(ABC):
    """
    Any connection used to instantiate an Emarsys object or an object inherited
     from BaseEndpoint should inherit from this class.
    this class.
    """

    @abstractmethod
    def __init__(self, username, secret, uri):
        self.username = username
        self.secret = secret
        self.uri = uri

    def build_authentication_variables(self):
        """
        Build the authentication variables Emarsys' authentication system
        asks for.
        :return: nonce, created, password_digest.
        """
        nonce = uuid.uuid4().hex
        created = datetime.datetime.utcnow().strftime(
            '%Y-%m-%dT%H:%M:%S+00:00'
        )
        sha1 = hashlib.sha1(
            str.encode(nonce + created + self.secret)
        ).hexdigest()
        password_digest = bytes.decode(base64.b64encode(str.encode(sha1)))
        return nonce, created, password_digest

    def build_headers(self, other_http_headers=None):
        """
        Build the headers Emarsys' authentication system asks for.
        :return: headers.
        """
        if not other_http_headers:
            other_http_headers = {}
        nonce, created, password_digest = \
            self.build_authentication_variables()

        wsse_header = ','.join(
            (
                'UsernameToken Username="{}"'.format(self.username),
                'PasswordDigest="{}"'.format(password_digest),
                'Nonce="{}"'.format(nonce),
                'Created="{}"'.format(created),
            )
        )
        http_headers = {
            'X-WSSE': wsse_header,
            'Content-Type': 'application/json',
        }
        http_headers.update(other_http_headers)
        return http_headers
