from nameko.rpc import rpc
from dependency.mongodb import MongoDatabase
from exceptions import NoArgument, NotFound


class SiteService(object):
    """Nameko service."""

    name = 'site_service'
    db = MongoDatabase(db_name='sites')

    @rpc
    def who_you_are(self):
        return 'I am site service'

    @rpc
    def get_sites(self):
        """Get all sites."""
        sites = self.db.sites.find()
        return self.process(sites)

    @staticmethod
    def process(data):
        """Process mongo cursor to list."""
        ret = list()
        for row in data:
            del row['_id']
            ret.append(row)
        return ret

    @rpc
    def get_site(self, url):
        """Get site by url."""
        pass
