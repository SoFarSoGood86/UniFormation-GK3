from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS
from datetime import timedelta
import random

SCAN_INTERVAL = timedelta(seconds=30)

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([
        UniFormationGK3TemperatureSensor(),
        UniFormationGK3JobSensor()
    ], True)

class UniFormationGK3TemperatureSensor(SensorEntity):
    def __init__(self):
        self._attr_name = "GK3 Température"
        self._attr_unique_id = "gk3_temp"
        self._attr_native_unit_of_measurement = TEMP_CELSIUS

    async def async_update(self):
        self._attr_native_value = 25 + random.randint(-2, 5)

class UniFormationGK3JobSensor(SensorEntity):
    def __init__(self):
        self._attr_name = "GK3 État impression"
        self._attr_unique_id = "gk3_job"

    async def async_update(self):
        self._attr_native_value = random.choice(["Idle", "Printing", "Paused"])
