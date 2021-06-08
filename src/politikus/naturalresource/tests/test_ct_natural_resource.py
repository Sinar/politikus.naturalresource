# -*- coding: utf-8 -*-
from politikus.naturalresource.content.natural_resource import INaturalResource  # NOQA E501
from politikus.naturalresource.testing import POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class NaturalResourceIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_NATURALRESOURCE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_natural_resource_schema(self):
        fti = queryUtility(IDexterityFTI, name='Natural Resource')
        schema = fti.lookupSchema()
        self.assertEqual(INaturalResource, schema)

    def test_ct_natural_resource_fti(self):
        fti = queryUtility(IDexterityFTI, name='Natural Resource')
        self.assertTrue(fti)

    def test_ct_natural_resource_factory(self):
        fti = queryUtility(IDexterityFTI, name='Natural Resource')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            INaturalResource.providedBy(obj),
            u'INaturalResource not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_natural_resource_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Natural Resource',
            id='natural_resource',
        )

        self.assertTrue(
            INaturalResource.providedBy(obj),
            u'INaturalResource not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('natural_resource', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('natural_resource', parent.objectIds())

    def test_ct_natural_resource_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Natural Resource')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_natural_resource_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Natural Resource')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'natural_resource_id',
            title='Natural Resource container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
