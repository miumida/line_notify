""" LINE Notify platform for notify component."""
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
from homeassistant.const import HTTP_OK
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

NOTIFY_LINE_API_URL = 'https://notify-api.line.me/api/notify'
CONF_TOKEN = "token"

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
        self._hass = hass
        self._token   = config.get(CONF_TOKEN)

        self._headers = {
            'Authorization' : 'Bearer {}'.format(self._token)
        }


    async def send_message(self, message="", **kwargs):
        """Send a message to specified target."""
        #websession = async_get_clientsession(self.hass)

        if len(message) > 1000:
            message = 'Message max length is 1000.'

        try:

            with async_timeout.timeout(10):

                data = {
                    "message": message
                }

                file = {}

                if kwargs is not None:
                    param = kwargs.get('data', None)
                    #sticker
                    if param and param.get('stickerId',False) and param.get('stickerPackageId', False):
                        stickerId        = kwargs['data']['stickerId']
                        stickerPackageId = kwargs['data']['stickerPackageId']

                        data["stickerId"]        = stickerId
                        data["stickerPackageId"] = stickerPackageId

                    #imageFile
                    if param and param.get('imageFile', False):
                        imageFile = kwargs['data']['imageFile']

                        file = { 'imageFile': open(imageFile, 'rb') }

                url = NOTIFY_LINE_API_URL

#                request = await websession.post(url, data=data, headers=self._headers)

                request = requests.post(url, headers=self._headers, data=data, files=file)

                if request.status_code != HTTP_OK:
                    _LOGGER.error( "Error %d on load URL %s", request.status_code, request.url)
                else:
                    _LOGGER.debug("Line Notify  send: %s", request.json())


        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Timeout for Line Notify")
