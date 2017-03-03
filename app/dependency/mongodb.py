"""Dependency Provider for MongoDB."""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from weakref import WeakKeyDictionary
from nameko.extensions import DependencyProvider


class MongoDatabase(DependencyProvider):

    def __init__(self, db_name='base'):
        self.databases = WeakKeyDictionary()
        self.client = None
        self.db_name = db_name

    def setup(self):
        connection_uri = self.container.config['MONGODB_URL']
        try:
            self.client = MongoClient(connection_uri)
        except ConnectionFailure as e:
            print 'Could not connect to MongoDB: {}'.format(e)

    def stop(self):
        self.client.close()
        del self.client

    def get_dependency(self, worker_ctx):
        _db = self.client[self.db_name]
        self.databases[worker_ctx] = _db
        return _db

    def worker_teardown(self, worker_ctx):
        db = self.databases.pop(worker_ctx)
