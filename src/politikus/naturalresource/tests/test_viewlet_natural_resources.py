# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from politikus.naturalresource.interfaces import IPolitikusNaturalresourceLayer
from politikus.naturalresource.testing import (
    POLITIKUS_NATURALRESOURCE_FUNCTIONAL_TESTING,
    POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING,
)
from Products.Five.browser import BrowserView
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager

import unittest


class ViewletIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Document', 'other-document')
        api.content.create(self.portal, 'News Item', 'newsitem')

    def test_natural_resources_is_registered(self):
        view = BrowserView(self.portal['other-document'], self.request)
        manager_name = 'plone.abovecontenttitle'
        alsoProvides(self.request, IPolitikusNaturalresourceLayer)
        manager = queryMultiAdapter(
            (self.portal['other-document'], self.request, view),
            IViewletManager,
            manager_name,
            default=None
        )
        self.assertIsNotNone(manager)
        manager.update()
        my_viewlet = [v for v in manager.viewlets if v.__name__ == 'natural-resources']  # NOQA: E501
        self.assertEqual(len(my_viewlet), 1)

    # XXX would be nice to have this test working:
    # def test_natural_resources_is_not_available_on_newsitem(self):
    #     view = BrowserView(self.portal['newsitem'], self.request)
    #     manager_name = 'plone.abovecontenttitle'
    #     alsoProvides(self.request, IPolitikusNaturalresourceLayer)
    #     manager = queryMultiAdapter(
    #         (self.portal['newsitem'], self.request, view),
    #         IViewletManager,
    #         manager_name,
    #         default=None
    #     )
    #     self.assertIsNotNone(manager)
    #     manager.update()
    #     my_viewlet = [v for v in manager.viewlets if v.__name__ == 'natural-resources']  # NOQA: E501
    #     self.assertEqual(len(my_viewlet), 0)


class ViewletFunctionalTest(unittest.TestCase):

    layer = POLITIKUS_NATURALRESOURCE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
