#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a school into the database"""
    mongo_collection.insert_one(kwargs)
    return (kwargs.get('_id'))
