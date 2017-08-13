# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.sortedquerystring


class CollectiveSortedquerystringLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.sortedquerystring)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.sortedquerystring:default')


COLLECTIVE_SORTEDQUERYSTRING_FIXTURE = CollectiveSortedquerystringLayer()


COLLECTIVE_SORTEDQUERYSTRING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SORTEDQUERYSTRING_FIXTURE,),
    name='CollectiveSortedquerystringLayer:IntegrationTesting'
)


COLLECTIVE_SORTEDQUERYSTRING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SORTEDQUERYSTRING_FIXTURE,),
    name='CollectiveSortedquerystringLayer:FunctionalTesting'
)


COLLECTIVE_SORTEDQUERYSTRING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SORTEDQUERYSTRING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveSortedquerystringLayer:AcceptanceTesting'
)
