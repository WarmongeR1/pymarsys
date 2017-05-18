# -*- coding: utf-8 -*-
__version__ = '0.0.1'
import sys

from pymarsys.connections.sync import SyncConnection
from pymarsys.emarsys import Emarsys

if sys.version_info >= (3, 5):
    from pymarsys.connections.async import AsyncConnection
