# -*- coding: utf-8 -*-
__version__ = '0.0.1'
import sys

from .connections.sync import SyncConnection
from .emarsys import Emarsys

if sys.version_info >= (3, 5):
    from .connections.async import AsyncConnection
