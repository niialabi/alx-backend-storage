#!/usr/bin/env python3
""" module contains update_topics func """


def update_topics(mongo_collection, name, topics):
    """ updated topics based on sch name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
