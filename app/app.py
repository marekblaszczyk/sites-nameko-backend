from nameko.rpc import rpc


class SiteService(object):
    """Nameko service."""

    name = 'site-service'

    @rpc
    def who_you_are(self):
        return 'I am site service'
