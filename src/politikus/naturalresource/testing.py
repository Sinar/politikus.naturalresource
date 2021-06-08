# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import politikus.naturalresource


class PolitikusNaturalresourceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=politikus.naturalresource)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'politikus.naturalresource:default')


POLITIKUS_NATURALRESOURCE_FIXTURE = PolitikusNaturalresourceLayer()


POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLITIKUS_NATURALRESOURCE_FIXTURE,),
    name='PolitikusNaturalresourceLayer:IntegrationTesting',
)


POLITIKUS_NATURALRESOURCE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLITIKUS_NATURALRESOURCE_FIXTURE,),
    name='PolitikusNaturalresourceLayer:FunctionalTesting',
)


POLITIKUS_NATURALRESOURCE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLITIKUS_NATURALRESOURCE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolitikusNaturalresourceLayer:AcceptanceTesting',
)
