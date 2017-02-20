# -*- coding: utf-8 -*-
from fabric.api import local



def run_app(layer=''):
    """This function lunches local server."""
    config_file = 'local.yaml'
    if layer == 'prod':
        config_file = 'local-prod.yaml'
    local('nameko run --config config/{} app.app'.format(config_file))
