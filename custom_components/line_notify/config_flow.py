"""Config flow for LINE Notify."""
import logging
import json

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN, TITLE, CONF_TOKEN, NOTIFY_LINE_API_URL

_LOGGER = logging.getLogger(__name__)


class LineNotifyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for LINE Notify."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize flow."""
        self._token: Required[str] = None

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            self._token    = user_input[CONF_TOKEN]

            uniqid = 'line-notify-{}'.format(user_input[CONF_TOKEN])
            await self.async_set_unique_id(uniqid)

            return self.async_create_entry(title=TITLE, data=user_input)

#        if self._async_current_entries():
#            return self.async_abort(reason="single_instance_allowed")

        if user_input is None:
            schema = vol.Schema(
                {
                    vol.Required(CONF_TOKEN, default=None): str
                }
            )

            return self.async_show_form(step_id='user', data_schema=schema)


    async def async_step_import(self, import_info):
        """Handle import from config file."""
        return await self.async_step_user(import_info)
