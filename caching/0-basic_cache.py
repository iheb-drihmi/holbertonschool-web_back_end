#!/usr/bin/python3
""" Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
