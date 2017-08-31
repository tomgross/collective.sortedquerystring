# -*- coding: utf-8 -*-
from collective.sortedquerystring import _
from collective.sortedquerystring.widget import SortableQueryStringFieldWidget
from plone.app.contenttypes.behaviors.collection import ICollection
from plone.app.contenttypes.behaviors.collection import Collection
from plone.autoform import directives as form
from plone.dexterity.interfaces import IDexterityContent
from zope import schema
from zope.component import adapter
from zope.interface import implementer_only
from zope.interface import provider
from plone.autoform.interfaces import IFormFieldProvider
from plone.batching import Batch


@provider(IFormFieldProvider)
class ISortableCollection(ICollection):

    form.widget('query', SortableQueryStringFieldWidget)

    sorting = schema.List(
        title=_(u'Sorting'),
        description=_(u'Widget specific sorting of the search results'),
        default=[],
        missing_value=[],
        value_type=schema.TextLine(),
        required=False,
    )

@implementer_only(ISortableCollection)
@adapter(IDexterityContent)
class SortableCollection(Collection):
    """ """

    def results(self, batch=True, b_start=0, b_size=None,
                sort_on=None, limit=None, brains=False,
                custom_query=None):
        results = super(SortableCollection, self).results(
            batch, b_start, b_size, sort_on, limit, brains, custom_query)
        positions = {j: i for i, j in enumerate(self.sorting)}
        results = sorted(
            results, key=lambda item: positions.get(item.uuid(), 999))
        if batch:
            results = Batch(results, b_size, start=b_start)
        return results

    @property
    def sorting(self):
        return getattr(self.context, 'sorting', [])

    @sorting.setter
    def sorting(self, value):
        self.context.sorting = value
