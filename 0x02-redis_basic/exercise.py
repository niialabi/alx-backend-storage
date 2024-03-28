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

def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ get data from cache using  key """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ get string from cache using key."""
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """ Get int from cache using key."""
        return int(self._redis.get(key))
