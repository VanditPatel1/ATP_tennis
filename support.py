import pandas as pd
from pprint import pprint

def total_unique(df, column):
    """
    Get total unique entries in a series
    and how many times it occured returned
    as a dict
    """

    series = df[column]
    unique = {}

    for key, value in series.iteritems():
        if value not in unique:
            unique[value] = 1

        else:
            unique[value] += 1

    return unique
