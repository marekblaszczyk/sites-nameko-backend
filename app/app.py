from nameko.rpc import rpc
from dependency.mongodb import MongoDatabase
from exceptions import NoArgument, NotFound
from pymongo.cursor import Cursor


class SiteService(object):
    """Nameko service."""

    name = 'site_service'
    db = MongoDatabase(db_name='sites')

    @rpc
    def who_you_are(self):
        return 'I am site service'

    @rpc
    def get_sites(self):
        """
        Get all sites.

        :return: List with site dicts
        """
        sites = self.db.sites.find()
        return self.process(sites)

    @rpc
    def get_site(self, url):
        """
        Get site by url.

        :param url: Url of page
        :return: Dict with site
        """

        site = self.db.sites.find_one({'url': url})
        return self.process(site)

    @staticmethod
    def process(data):
        """Process data parameter."""
        if isinstance(data, Cursor):
            ret = list()
            for row in data:
                del row['_id']
                ret.append(row)
            return ret
        if isinstance(data, dict):
            del data['_id']
            return data
