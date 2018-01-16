# -*- Coding: UTF-8 -*-
import falcon

from blockchain_api.extensions import print_log_middleware as plm
from blockchain_api.resources import api_resource as api_rsc


def create_api():
    api = falcon.API(middleware=plm.PrintLogMiddleware())
    api.add_route('/mine', api_rsc.Mine())
    api.add_route('/transaction/new', api_rsc.NewTransaction())
    api.add_route('/chain', api_rsc.FullChain())
    return api


app = create_api()
