#!/usr/bin/env python3
""" contains cache class """

import redis
import uuid
from typing import Union, Any, Callable


def count_calls(method: Callable) -> Callable:
    """ Decorator to count the number of calls to a class method """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """ Wrapper function that increments a key in Redis for Cache.store """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    """ Cache Class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
