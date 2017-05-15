# -*- coding: utf-8 -*-

import asyncio
import sys
from unittest import TestCase
from urllib.parse import urljoin

import pytest
from aioresponses import aioresponses

from pymarsys.connections import AsyncConnection

EMARSYS_URI = 'https://api.emarsys.net/'
TEST_USERNAME = 'test_username'
TEST_SECRET = 'test_secret'

EMARSYS_SETTINGS_RESPONSE = {
    'data': {
        'country': 'France',
        'environment': 'suite16.emarsys.net',
        'id': 123456789,
        'name': 'testname',
        'password_history_queue_size': 1,
        'timezone': 'Europe/Paris',
        'totalContacts': '111111'
    },
    'replyCode': 0,
    'replyText': 'OK'
}


@pytest.mark.skipif(sys.version_info < (3, 5), reason="requires python3.5")
class TestAsyncConnection(TestCase):
    def test_init(self):
        connection = AsyncConnection(
            TEST_USERNAME,
            TEST_SECRET,
            EMARSYS_URI
        )

        assert connection.username == TEST_USERNAME
        assert connection.secret == TEST_SECRET
        assert connection.uri == EMARSYS_URI

    def test_make_call(self):
        connection = AsyncConnection(
            TEST_USERNAME,
            TEST_SECRET,
            EMARSYS_URI
        )
        with aioresponses() as m:
            m.get(
                urljoin(EMARSYS_URI, 'api/v2/settings'),
                status=200,
                payload=EMARSYS_SETTINGS_RESPONSE
            )
            coroutine = connection.make_call('GET', 'api/v2/settings')
            loop = asyncio.get_event_loop()
            response = loop.run_until_complete(coroutine)
            assert response == EMARSYS_SETTINGS_RESPONSE
