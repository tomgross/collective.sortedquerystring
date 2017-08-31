.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================
collective.sortablequerystring
==============================

Provide a customized querystring widget, which allows sorting.

Requirements: Plone 5.1

Features
--------

- Can be used with collection behavior
- Can be used with listing tile of plone.app.standardtiles

Examples
--------



Installation
------------

Install collective.sortedquerystring by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.sortedquerystring


and then running ``bin/buildout``

Development
-----------

Build mockup

$ bin/plone-compile-resources -s Plone -b plone
$ bin/plone-compile-resources -s Plone -b plone-logged-in

Build resources

$ bin/plone-compile-resources -s Plone -b sortablequerystring

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.sortedquerystring/issues
- Source Code: https://github.com/collective/collective.sortedquerystring
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
