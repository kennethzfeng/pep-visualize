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
      var height = 500;
      var chart = d3.select('#chart')
        .attr('width', width)
        .attr('height', height);

      var xScale = d3.scale.linear()
        .domain([0, d3.max(json.data, function(d) {
            return d.count;
          })])
        .range([0, width]);


      var bar = chart.selectAll('g')
          .data(json.data)
        .enter().append('g')
          .attr('transform', function(d, i) { return 'translate(0, ' + 20 * i + ')'; });

      bar.append('rect')
          .attr('width', function(d) { return xScale(d.count); })
          .attr('height', 19);

      bar.append('text')
          .attr('x', function(d) { return xScale(d.count) - 3; })
          .attr('y', function(d) { return 20 / 2; })
          .attr('dy', '.35em')
          .text(function(d) { return d.count; });


    });


  });
});
