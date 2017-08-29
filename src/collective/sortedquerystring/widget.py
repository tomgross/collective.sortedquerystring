# -*- coding: utf-8 -*-
from plone.app.z3cform.widget import IQueryStringWidget
from plone.app.z3cform.widget import QueryStringWidget
from zope.interface import implementer_only

__author__ = 'Team Web <webmaster@fhnw.ch'


class ISortableQueryStringWidget(IQueryStringWidget):
    """

    """


@implementer_only(ISortableQueryStringWidget)
class SortableQueryStringWidget(QueryStringWidget):
    """QueryString widget for z3c.form."""

    pattern = 'sortablequerystring'
    pattern_options = QueryStringWidget.pattern_options.copy()

    def _base_args(self):
        """Method which will calculate _base class arguments.

        Returns (as python dictionary):
            - `pattern`: pattern name
            - `pattern_options`: pattern options
            - `name`: field name
            - `value`: field value

        :returns: Arguments which will be passed to _base
        :rtype: dict
        """
        args = super(SortableQueryStringWidget, self)._base_args()
        args['pattern_options']['previewURL'] = args['pattern_options']['previewURL'].replace(
            'querybuilder_html_results', 'sortable_querybuilder_html_results', 1)
        return args

# EOF
