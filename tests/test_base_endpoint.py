# -*- coding: utf-8 -*-

from unittest import TestCase

import pytest

from pymarsys.base_endpoint import BaseEndpoint


class TestBaseEndpoint(TestCase):
    def test_init(self):
        with pytest.raises(TypeError) as excinfo:
            BaseEndpoint()
        assert "Can't instantiate abstract class BaseEndpoint with abstract " \
               "methods __init__" in str(excinfo.value)
