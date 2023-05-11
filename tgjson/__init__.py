"""
tgjson
"""
__version__ = "0.1.0"
__author__ = "ffernandoalves"

import json
from tgjson.core import TgJSON

__all__ = ["TgJson", "dumps", "loads"]

def dumps(data: dict):
    return json.dumps(data, cls=TgJSON.Encoder)

def loads(data: str):
    return json.loads(data, cls=TgJSON.Decoder)