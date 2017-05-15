# -*- coding: utf-8 -*-
from unittest import TestCase

from pymarsys.connections import SyncConnection
from pymarsys.contact import Contact
from pymarsys.emarsys import Emarsys

EMARSYS_URI = 'https://api.emarsys.net/'
TEST_USERNAME = 'test_username'
TEST_SECRET = 'test_secret'


class TestEmarsys(TestCase):
    def test_init_no_exception(self):
        connection = SyncConnection(TEST_USERNAME, TEST_SECRET)
        client = Emarsys(connection)

        isinstance(client.connection, SyncConnection)
        isinstance(client.contacts, Contact)
