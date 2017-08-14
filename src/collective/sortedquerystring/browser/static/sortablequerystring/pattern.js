define([
  'jquery',
  'mockup-patterns-querystring',
  'mockup-patterns-sortable',
], function($, QueryString, Sortable) {
  'use strict';

  var SortableQueryString = QueryString.extend({
    name: 'sortablequerystring',
    trigger: '.pat-sortablequerystring',
    parser: 'mockup',
    defaults: {
    },
    refreshPreviewEvent: function(value) {
      var self = this;

      if (!self.options.showPreviews) {
        return; // cut out of this if there are no previews available
      }

      if (typeof self._previewXhr !== 'undefined') {
        self._previewXhr.abort();
      }

      if (typeof self.$previewPane !== 'undefined') {
        self.$previewPane.remove();
      }

      var query = [], querypart;
      $.each(self.criterias, function(i, criteria) {
        var querypart = criteria.buildQueryPart();
        if (querypart !== '') {
          query.push(querypart);
        }
      });

      self.$previewPane = $('<div/>')
        .addClass(self.options.classPreviewName)
        .appendTo(self.$previewWrapper);

      if (query.length <= 0) {
        $('<div/>')
          .addClass(self.options.classPreviewCountWrapperName)
          .html('No results to preview')
          .prependTo(self.$previewPane);
        return; // no query means nothing to send out requests for
      }

      query.push('sort_on=' + self.$sortOn.val());
      if (self.$sortOrder.prop('checked')) {
        query.push('sort_order=reverse');
      }
      self._previewXhr = $.get(self.options.previewURL + '?' + query.join('&'))
          .done(function(data, stat) {
            $('<div/>')
              .addClass(self.options.classPreviewResultsWrapperName)
              .html(data)
              .appendTo(self.$previewPane);
            console.log('hi');
          });
    },
  });

  return SortableQueryString;
});
