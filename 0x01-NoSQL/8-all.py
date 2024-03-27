#!/usr/bin/env python3
""" module contains list_all func """


def list_all(mongo_collection):
    """ lists all docs in mongo coll """
    return mongo_collection.find()
