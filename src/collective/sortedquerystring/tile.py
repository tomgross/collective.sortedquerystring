# -*- coding: utf-8 -*-
from collective.sortedquerystring import _
from collective.sortedquerystring.widget import SortableQueryStringFieldWidget
from plone.app.standardtiles import contentlisting
from plone.autoform import directives as form
from zope import schema
from zope.component import getMultiAdapter
from zope.interface import alsoProvides


__author__ = 'Tom Gross <itconsense@gmail.com>'


class ISortableContentListingTile(contentlisting.IContentListingTile):

    form.widget('query', SortableQueryStringFieldWidget)

    sorting = schema.List(
        title=_(u'Sorting'),
        description=_(u'Widget specific sorting of the search results'),
        default=[],
        missing_value=[],
        value_type=schema.TextLine(),
        required=False,
    )


class SortableContentListingTile(contentlisting.ContentListingTile):

    def contents(self):
        """Search results"""
        builder = getMultiAdapter(
            (self.context, self.request),
            name='querybuilderresults'
        )
        results = builder(
            query=self.query,
            sort_on=self.sort_on or 'getObjPositionInParent',
            sort_order=self.sort_order,
            limit=self.limit
        )
        sorting = self.data.get('sorting', '')
        positions = {j: i for i, j in enumerate(sorting)}
        results = sorted(
            results, key=lambda item: positions.get(item.uuid(), 999))
        print(results)

        view = self.view_template or 'listing_view'
        view = view.encode('utf-8')
        options = dict(original_context=self.context)
        alsoProvides(self.request, contentlisting.IContentListingTileLayer)
        return getMultiAdapter((results, self.request), name=view)(**options)

# EOF
