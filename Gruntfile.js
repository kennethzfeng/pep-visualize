'use strict';

module.exports = function(grunt) {

  // Project Configuratioin
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    bower: {
      install: {
        options: {
          targetDir: './app/static/lib',
          install: true,
          copy: false,
          verbose: true,
          cleanTargetDir: true,
          layout: 'byComponent'
        }
      }
    }

  });


  grunt.loadNpmTasks('grunt-bower-task');

  grunt.registerTask('default', []);
  grunt.registerTask('install', ['bower']);
  grunt.registerTask('heroku:production', ['install']);

};
