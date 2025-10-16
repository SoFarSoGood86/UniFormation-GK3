import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

class UniFormationGK3ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_NAME, default="UniFormation GK3"): str,
            vol.Required(CONF_HOST): str
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
