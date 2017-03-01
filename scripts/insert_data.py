"""Add example data to mongo db."""
import csv
from pymongo import MongoClient


def connect():
    """Connect to mongo"""
    client = MongoClient('mongodb://localhost:27017/')
    return client


def insert_data(connection, row):
    """Insert each row to mongo collection."""
    db = connection[row[0]]
    collection = db[row[0]]

    site = {'url': row[1], 'title': row[2], 'content': row[3]}
    collection.update({'url': site['url']}, site, upsert=True)


if __name__ == '__main__':
    connection = connect()
    with open('data.csv', 'rb') as csvfile:
        rowreader = csv.reader(csvfile, delimiter=';')
        for row in rowreader:
            insert_data(connection, row)

    print "Sites added/updated."
