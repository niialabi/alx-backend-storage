#!/usr/bin/env python3
""" contains cache class """

import redis
import uuid
from typing import Union


class Cache:
    """ Cache Class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method takes data argument and ret string """
        r_key = str(uuid.uuid1())
        self._redis.set(r_key, data)
        return r_key


