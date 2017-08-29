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


from plone.supermodel import model

@provider(IFormFieldProvider)
class ISortableCollection(ICollection):

    # query = schema.List(
    #     title=_(u'Search terms'),
    #     description=_(u'Define the search terms for the items you want '
    #                   u'to list by choosing what to match on. '
    #                   u'The list of results will be dynamically updated'),
    #     value_type=schema.Dict(value_type=schema.Field(),
    #                            key_type=schema.TextLine()),
    #     required=False,
    #     missing_value=''
    # )
    form.widget('query', SortableQueryStringFieldWidget)

    sorting = schema.List(
        title=_(u'Sorting'),
        description=_(u'Widget specific sorting of the search results'),
        default=[],
        value_type=schema.TextLine(),
        required=False,
    )


@implementer_only(ISortableCollection)
@adapter(IDexterityContent)
class SortableCollection(Collection):
    """ """
