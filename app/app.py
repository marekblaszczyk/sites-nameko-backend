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
    def get_site(self, site_id=None, url=None):
        """
        Get site by url or site_id.

        :param site_id: id of looking site
        :param url: Url of page
        :return: Dict with site
        """

        if site_id:
            site = self.db.sites.find_one({'site_id': str(site_id)})
        elif url:
            site = self.db.sites.find_one({'url': url})
        else:
            raise NoArgument('Give me site_id or url.')

        if site is None:
            raise NotFound('No site with this site_id or url.')

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
