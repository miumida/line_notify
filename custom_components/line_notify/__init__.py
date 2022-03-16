from http import HTTPStatus
import requests
import logging
import asyncio
import aiohttp
import async_timeout

import json
import base64

import voluptuous as vol

import homeassistant.loader as loader
from homeassistant.const import (STATE_UNKNOWN, EVENT_STATE_CHANGED)
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from homeassistant.helpers import discovery

from .const import DOMAIN, CONF_TOKEN, NOTIFY_LINE_API_URL

_LOGGER = logging.getLogger(__name__)


def base_config_schema(config: dict = {}) -> dict:
    """Return a shcema configuration dict for LINE Notify."""
    if not config:
        config = {
            CONF_TOKEN: "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }
    return {
        vol.Required(CONF_TOKEN, default=config.get(CONF_TOKEN)): str,
    }


def config_combined() -> dict:
    """Combine the configuration options."""
    base = base_config_schema()

    return base

CONFIG_SCHEMA = vol.Schema({DOMAIN: config_combined()}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass, config):

    if DOMAIN not in config:
        return True

    return True


async def async_setup_entry(hass, config_entry):
    """Set up this integration using UI."""

    if hass.data.get(DOMAIN) is not None:
        return False

    if config_entry.source == config_entries.SOURCE_IMPORT:
        hass.async_create_task(hass.config_entries.async_remove(config_entry.entry_id))
        return False

    token = config_entry.data[CONF_TOKEN]

    hdr = {
        'Authorization' : 'Bearer {}'.format(token)
    }

    session = async_get_clientsession(hass)

    # speak add service
    async def send_message(service):
        message = service.data["message"]

        if len(message) > 1000:
            message = 'Message max length is 1000.'
            _LOGGER.error(f'[{DOMAIN}] send_message() Error, %s', message)

        try:
            with async_timeout.timeout(90):
                data = { "message": message }

                if ( "stickerId" in service.data ) and ( "stickerPackageId" in service.data ):
                    data["stickerId"]        = service.data["stickerId"]
                    data["stickerPackageId"] = service.data["stickerPackageId"]

                file = {}

                url = NOTIFY_LINE_API_URL

                request = await session.post(url, headers=hdr, data=data)

                if request.status != HTTPStatus.OK:
                    _LOGGER.error( f"[{DOMAIN}] Error %d on load URL : %s", request.status, request.url)
                else:
                    _LOGGER.debug(f"[{DOMAIN}] send_message : %s", await request.json())

        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error(f"[{DOMAIN}] Timeout Error.")


    hass.services.async_register(DOMAIN, "send_message", send_message)

    return True

