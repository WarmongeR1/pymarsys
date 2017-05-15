# -*- coding: utf-8 -*-
from unittest import TestCase
from urllib.parse import urljoin

import responses

from pymarsys.connections import SyncConnection

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


class TestSyncConnection(TestCase):
    def test_init(self):
        connection = SyncConnection(TEST_USERNAME, TEST_SECRET, EMARSYS_URI)

        assert connection.username == TEST_USERNAME
        assert connection.secret == TEST_SECRET
        assert connection.uri == EMARSYS_URI

    @responses.activate
    def test_make_call(self):
        responses.add(
            responses.GET,
            urljoin(EMARSYS_URI, 'api/v2/settings'),
            json=EMARSYS_SETTINGS_RESPONSE,
            status=200,
            content_type='application/json'
        )
        connection = SyncConnection(TEST_USERNAME, TEST_SECRET, EMARSYS_URI)

        response = connection.make_call('GET', 'api/v2/settings')
        assert response == EMARSYS_SETTINGS_RESPONSE
