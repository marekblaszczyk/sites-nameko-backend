# -*- coding: utf-8 -*-
from fabric.api import local


def test():
    """This is a test runner. It runs tests with coverage, prints and generates a report."""
    local('py.test -s -v --cov-config=.coveragerc --cov=. --cov-report term-missing --cov-report html --cov-report xml --junitxml build/results.xml')


def run_app(layer=''):
    """This function lunches local server."""
    config_file = 'local.yaml'
    if layer == 'prod':
        config_file = 'local-prod.yaml'
    local('nameko run --config config/{} app.app'.format(config_file))
