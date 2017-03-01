"""Test service."""
import pytest

def test_who_you_are(service):

    result = service.who_you_are()

    assert isinstance(result, str) is True
    assert result == 'I am site service'


@pytest.mark.parametrize('no, data', [
    (1, True),
    (2, False)
])
def test_get_sites(service, sites, no, data):

    if data is True:
        service.db.sites.find.return_value = sites
        result = service.get_sites()
        assert isinstance(result, list) is True
        assert len(result) == 3
        assert result == [{u'url': u'/', u'content': u'Home page content', u'title': u'Home page'},
                          {u'url': u'/about', u'content': u'about page content', u'title': u'About Page'},
                          {u'url': u'/contact', u'content': u'contact page content', u'title': u'Contact Page'}]

    if data is False:
        service.db.sites.find.return_value = []
        result = service.get_sites()
        assert isinstance(result, list) is True
        assert len(result) == 0
        assert result == []
