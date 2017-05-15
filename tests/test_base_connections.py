# -*- coding: utf-8 -*-

import datetime
from unittest import TestCase

from pymarsys.connections import BaseConnection

EMARSYS_URI = 'https://api.emarsys.net/'
TEST_USERNAME = 'test_username'
TEST_SECRET = 'test_secret'


class TestBaseConnection(TestCase):
    def test_build_authentication_variables(self):
        BaseConnection.__abstractmethods__ = frozenset()
        connection = BaseConnection(TEST_USERNAME, TEST_SECRET, EMARSYS_URI)
        nonce, created, password_digest = \
            connection.build_authentication_variables()
        assert len(nonce) == 32
        assert int(nonce, 16)
        date_exceptions = 0
        for date_format in ('%Y-%m-%dT%H:%M:%S+00:00',
                            '%Y-%m-%dT%H:%M:%S',
                            '%Y-%m-%dT%H:%M:%S+0000'):
            try:
                datetime.datetime.strptime(created, date_format)
            except ValueError:
                date_exceptions += 1
        assert date_exceptions == 2
        assert len(created) == 25
        assert len(password_digest) == 56
