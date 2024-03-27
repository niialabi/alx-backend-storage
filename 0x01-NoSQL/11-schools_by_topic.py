#!/usr/bin/env python3
""" module for schools_by_topic func """


def schools_by_topic(mongo_collection, topic):
    """ function list of school having a specified topic """
    return mongo_collection.find({"topics": topic})
