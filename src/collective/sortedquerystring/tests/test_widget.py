# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.sortedquerystring.testing import COLLECTIVE_SORTEDQUERYSTRING_INTEGRATION_TESTING  # noqa

import unittest


class TestView(unittest.TestCase):
    """Test that collective.sortedquerystring is properly installed."""

    layer = COLLECTIVE_SORTEDQUERYSTRING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.query = [{
            'i': 'portal_type',
            'o': 'plone.app.querystring.operation.string.is',
            'v': 'Document',
        }]
        self.view = api.content.get_view(
            name='sortable_querybuilder_html_results',
            context=self.portal,
            request=self.request
        )

    def test_html_query_result_noresults(self):
        """Test rendering of sorted html query result."""
        self.assertIn(
            '<strong id="search-results-number">0</strong> items matching your search terms.',  # noqa
            self.view.html_results(self.query)
        )

    def test_html_query_result_list(self):
        """
        :return:
        """
        setRoles(self.portal, TEST_USER_ID, ['Manager', ])
        doc1 = api.content.create(self.portal, 'Document', title='A doc')
        doc1.reindexObject()
        self.assertIn(
            '<a href="http://nohost/plone/a-doc" class="state-private contenttype-document">A doc</a>', # noqa
            self.view.html_results(self.query)
        )
