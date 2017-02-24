from nameko.rpc import rpc
from dependency.mongodb import MongoDatabase


class SiteService(object):
    """Nameko service."""

    name = 'site_service'
    db = MongoDatabase()
    print db

    @rpc
    def who_you_are(self):
        return 'I am site service'

    @rpc
    def get_sites(self):
        # print self.db
        # print self.db.sites
        sites = self.db.sites.find()
        # print sites
        # print sites.__dict__
        for site in sites:
            print site
        return 1