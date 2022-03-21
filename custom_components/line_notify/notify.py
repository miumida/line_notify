""" LINE Notify platform for notify component."""
from http import HTTPStatus
import logging
import asyncio
import io

import aiohttp
import async_timeout

import requests
from requests.auth import HTTPBasicAuth
import voluptuous as vol

from homeassistant.components.notify import (
    PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN, CONF_TOKEN, NOTIFY_LINE_API_URL

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_TOKEN): cv.string,
    }
)

def get_service(hass, config, discovery_info=None):
    """Get the LINE Notify notification service."""
    return LineNotificationService(hass, config)


class LineNotificationService(BaseNotificationService):
    """Implementation of the notification service for LINE Notify"""

    def __init__(self, hass, config):
        """Initialize the service."""
        self._hass  = hass
        self._token  = config.get(CONF_TOKEN)

        self._headers = {
            'Authorization' : 'Bearer {}'.format(self._token)
        }


    def send_message(self, message="", **kwargs):
        """Send a message to specified target."""

        if len(message) > 1000:
            _LOGGER.error("[Error] Message max length is 1000. Input message is [ %s ]", message)

        data = {
                "message": message
               }

        file = {}

        param = kwargs.get('data', None)

        if param is not None:
            #sticker
            if ( "stickerId" in param ) and ( "stickerPackageId" in param ):
                data["stickerId"]        = param["stickerId"]
                data["stickerPackageId"] = param["stickerPackageId"]

            #imageFile
            if "imageFile" in param:
                imageFile = param["imageFile"]
                file = { 'imageFile': open(imageFile, 'rb') }

        url = NOTIFY_LINE_API_URL

        request = requests.post(url, headers=self._headers, data=data, files=file)

        if request.status_code != HTTPStatus.OK:
            _LOGGER.error( f"[{DOMAIN}] Error %d on load URL %s", request.status_code, request.url)
            _LOGGER.error( f"[{DOMAIN}] Error -> %s", request.json())
        else:
            _LOGGER.debug(f"[{DOMAIN}] Line Notify  send: %s", request.json())
