#!/usr/bin/env python3
"""Python function that changes all topics of a school document based"""


def update_topics(mongo_collection, name, topics):
    """Updates a school's topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return True
