#!/usr/bin/python3
""" This module contains the LIFOCache class. """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A class that represents a Last-In-First-Out (LIFO) cache. """

    def __init__(self):
        """ Initialize an instance of LIFOCache. """
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache. """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.keys.pop()
            print("DISCARD: " + last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
