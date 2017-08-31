# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.app.contenttypes.browser.collection import CollectionView
from collective.sortedquerystring.behavior import SortableCollection


class SortableCollectionView(CollectionView):

    @property
    def collection_behavior(self):
        context = aq_inner(self.context)
        return SortableCollection(context)
