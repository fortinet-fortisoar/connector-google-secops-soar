"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from django.utils.module_loading import import_string
from .constants import LOGGER_NAME
from .custom_connector import CustomConnector

logger = get_logger(LOGGER_NAME)


class BaseConnector(Connector):
    def execute(self, config: dict, operation: str, params: dict, *args, **kwargs):
        return supported_operations.get(operation)(config, params)

    def check_health(self, config: dict = None, *args, **kwargs):
        return check_health(config, *args, **kwargs)
        # return True


def check_health(config):
    try:
        conn = CustomConnector(config)
        return conn.check_health(config)
    except Exception as e:
        raise ConnectionError(e.str)


def generic_api_call(config: dict, params: dict):
    try:
        conn = CustomConnector(config)
        return conn.generic_api_call(config, params)
    except Exception as e:
        raise ConnectionError(e.str)


supported_operations = {
    "check_health": check_health,
    "generic_api_call": generic_api_call
}
