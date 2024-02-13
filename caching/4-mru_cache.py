#!/usr/bin/python3
""" Module for MRUCache class """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Most Recently Used (MRU) Cache implementation """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently = self.keys.pop()
            del self.cache_data[most_recently]
            print("DISCARD: " + most_recently)
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
