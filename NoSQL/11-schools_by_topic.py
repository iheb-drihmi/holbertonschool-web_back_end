#!/usr/bin/env python3
"""Python function that returns the list"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list"""
    return list(mongo_collection.find({"topics": {"$all": [topic]}}))