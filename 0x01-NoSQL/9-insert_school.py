#!/usr/bin/env python3
""" Module contains insert sch func """


def insert_school(mongo_collection, **kwargs):
    """ inserts kwargs into collection """
    ins = mongo_collection.insert_one(kwargs)
    return ins.inserted_id
