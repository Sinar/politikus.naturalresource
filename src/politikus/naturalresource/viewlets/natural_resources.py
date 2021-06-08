# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.interfaces import IVocabularyFactory


class NaturalResources(ViewletBase):

    def render(self):
        return super(NaturalResources, self).render()
