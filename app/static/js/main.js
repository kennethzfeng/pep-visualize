'use strict';

require.config({
  paths: {
    jquery: '/static/lib/jquery/dist/jquery.min',
    bootstrap: '/static/lib/bootstrap/dist/js/bootstrap.min',
    d3: '/static/lib/d3/d3.min'
  },
  shim: {
    'jquery': { 'exports' : 'jquery' },
    'bootstrap': ['jquery']
  }
});

require(['d3', 'bootstrap', 'jquery'], function(d3) {
  console.log('Loaded');

  $(document).ready(function() {
    var data = d3.json('/pep/stat', function(error, json) {

      console.log(json.data);

      var chart = d3.select('#chart');

      chart.selectAll('div')
        .data(json.data)
        .enter().append('div')
          .style('width', function(d) { return d.count * 10 + 'px'; })
          .text(function(d) { return d.count; });
    });


  });
});
