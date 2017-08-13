# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.sortedquerystring.testing import COLLECTIVE_SORTEDQUERYSTRING_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.sortedquerystring is properly installed."""

    layer = COLLECTIVE_SORTEDQUERYSTRING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.sortedquerystring is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.sortedquerystring'))

    def test_browserlayer(self):
        """Test that ICollectiveSortedquerystringLayer is registered."""
        from collective.sortedquerystring.interfaces import (
            ICollectiveSortedquerystringLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveSortedquerystringLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SORTEDQUERYSTRING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.sortedquerystring'])

    def test_product_uninstalled(self):
        """Test if collective.sortedquerystring is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.sortedquerystring'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveSortedquerystringLayer is removed."""
        from collective.sortedquerystring.interfaces import \
            ICollectiveSortedquerystringLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveSortedquerystringLayer,
           utils.registered_layers())
