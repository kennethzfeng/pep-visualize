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

      var width = 800;
      var chart = d3.select('#chart')
        .attr('width', width);

      var xScale = d3.scale.linear()
        .domain([0, d3.max(json.data, function(d) {
            return d.count;
          })])
        .range([0, width]);


      chart.selectAll('div')
        .data(json.data)
        .enter().append('div')
          .style('width', function(d) { return xScale(d.count) + 'px'; })
          .text(function(d) { return d.count; });
    });


  });
});
