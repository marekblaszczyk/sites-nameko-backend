"""Test fixtures."""
import pytest
from nameko.testing.services import worker_factory
from app.app import SiteService


class ObjectId(object):

    def __init__(self, _id):
        self._id = _id


@pytest.fixture(scope='function')
def service():
    return worker_factory(SiteService)


@pytest.fixture(scope='function')
def sites():
    return [
        {u'_id': ObjectId('58b09d8ca05cc5c3fa739453'), u'url': u'/', u'content': u'Home page content', u'title': u'Home page'},
        {u'_id': ObjectId('58b09d8ea05cc5c3fa739454'), u'url': u'/about', u'content': u'about page content', u'title': u'About Page'},
        {u'_id': ObjectId('58b09d91a05cc5c3fa739455'), u'url': u'/contact', u'content': u'contact page content', u'title': u'Contact Page'}
    ]
