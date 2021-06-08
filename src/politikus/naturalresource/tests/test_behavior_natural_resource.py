# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from politikus.naturalresource.behaviors.natural_resource import INaturalResourceMarker
from politikus.naturalresource.testing import (
    POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING  # noqa,
)
from zope.component import getUtility

import unittest


class NaturalResourceIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_natural_resource(self):
        behavior = getUtility(IBehavior, 'politikus.naturalresource.natural_resource')
        self.assertEqual(
            behavior.marker,
            INaturalResourceMarker,
        )
