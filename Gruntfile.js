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
    },

    shell: {
      pythonServer: {
        options: {
          stdout: true
        },
        command: 'env/bin/python run_dev_server.py'
      },

      virtualenv: {
        options: {
          stdout: true
        },
        command: 'virtualenv env'
      },

      pythonDeps: {
        options: {
          stdout: true
        },
        command: 'env/bin/pip install -r requirements.txt'
      }
    }

  });


  grunt.loadNpmTasks('grunt-bower-task');
  grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('default', []);
  grunt.registerTask('install', ['bower']);
  grunt.registerTask('heroku:production', ['install']);
  grunt.registerTask('dev:setup', ['shell:virtualenv', 'shell:pythonDeps']);
  grunt.registerTask('dev:server', ['dev:setup', 'shell:pythonServer']);


};
