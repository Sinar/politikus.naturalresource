# -*- coding: utf-8 -*-

from politikus.naturalresource import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.autoform import directives
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource


class INaturalResourceMarker(Interface):
    pass


@provider(IFormFieldProvider)
class INaturalResource(model.Schema):
    """
    """

    directives.widget('natural_resources',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    natural_resources = RelationList(
            title=u'Natural Resources',
            description=_(u'''
            Related Natural Resources
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='Natural Resource'),
                ),
            required=False,
            )

@implementer(INaturalResource)
@adapter(INaturalResourceMarker)
class NaturalResource(object):
    def __init__(self, context):
        self.context = context

    @property
    def natural_resources(self):
        if safe_hasattr(self.context, 'natural_resources'):
            return self.context.natural_resources
        return None

    @natural_resources.setter
    def natural_resources(self, value):
        self.context.natural_resources = value
