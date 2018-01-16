# -*- Coding: UTF-8 -*-
from blockchain_api.logger import get_logger

LOGGER = get_logger(__name__)


class PrintLogMiddleware(object):

    def process_request(self, req, resp):
        LOGGER.info("⚡️ >>> Request info < Host:{}, Method:{}, Path:{} >.".format(req.host, req.method, req.path,))
        LOGGER.info("⚡️ >>> Request Body:{} \n".format(req.stream.read().decode('utf-8')))

    def process_resource(self, req, resp, resource, param):
        LOGGER.info("🎁  >>> Resource info < Type:{} >.\n".format(type(resource)))

    def process_response(self, req, resp, resource):
        LOGGER.info("🌙  >>> Response info < Body:{}, Status:{} >.\n".format(resp.body, resp.status))
