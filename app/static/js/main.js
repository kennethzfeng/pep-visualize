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

require(['bootstrap', 'jquery', 'd3'], function() {
  console.log('Loaded');
});
