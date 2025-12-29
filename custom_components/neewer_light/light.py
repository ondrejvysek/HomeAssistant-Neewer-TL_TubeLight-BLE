"""Platform for Neewer Tube Light integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_COLOR_TEMP,
    ATTR_RGB_COLOR,
    ColorMode,
    LightEntity,
    LightEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_DEVICE_ID, CONF_MODEL, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    MAX_MIREDS,
    MIN_MIREDS,
    MODEL_TL120C,
    MODEL_TL60_RGB,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Neewer Tube Light from a config entry."""
    device_id = config_entry.data[CONF_DEVICE_ID]
    model = config_entry.data[CONF_MODEL]
    name = config_entry.data[CONF_NAME]

    light = NeewerTubeLight(device_id, model, name, config_entry)
    async_add_entities([light])


class NeewerTubeLight(LightEntity):
    """Representation of a Neewer Tube Light."""

    _attr_has_entity_name = True
    _attr_name = None

    def __init__(
        self,
        device_id: str,
        model: str,
        name: str,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize the Neewer Tube Light."""
        self._device_id = device_id
        self._model = model
        self._name = name
        self._config_entry = config_entry
        self._attr_unique_id = f"{device_id}_light"

        # Set supported features based on model
        if model == MODEL_TL60_RGB:
            self._attr_supported_color_modes = {ColorMode.RGB}
            self._attr_color_mode = ColorMode.RGB
        elif model == MODEL_TL120C:
            self._attr_supported_color_modes = {ColorMode.COLOR_TEMP, ColorMode.RGB}
            self._attr_color_mode = ColorMode.COLOR_TEMP
            self._attr_min_mireds = MIN_MIREDS
            self._attr_max_mireds = MAX_MIREDS
        else:
            self._attr_supported_color_modes = {ColorMode.BRIGHTNESS}
            self._attr_color_mode = ColorMode.BRIGHTNESS

        # Initial state
        self._attr_is_on = False
        self._attr_brightness = 255
        self._attr_rgb_color = (255, 255, 255)
        self._attr_color_temp = MIN_MIREDS

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information about this Neewer Tube Light."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._device_id)},
            name=self._name,
            manufacturer="Neewer",
            model=self._model,
            sw_version="1.0.0",
        )

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn on the light."""
        self._attr_is_on = True

        if ATTR_BRIGHTNESS in kwargs:
            self._attr_brightness = kwargs[ATTR_BRIGHTNESS]

        if ATTR_RGB_COLOR in kwargs:
            self._attr_rgb_color = kwargs[ATTR_RGB_COLOR]
            if self._model == MODEL_TL120C:
                self._attr_color_mode = ColorMode.RGB

        if ATTR_COLOR_TEMP in kwargs and self._model == MODEL_TL120C:
            self._attr_color_temp = kwargs[ATTR_COLOR_TEMP]
            self._attr_color_mode = ColorMode.COLOR_TEMP

        # Send command to ESPHome device
        await self._send_command()

        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the light."""
        self._attr_is_on = False

        # Send command to ESPHome device
        await self._send_command()

        self.async_write_ha_state()

    async def _send_command(self) -> None:
        """Send command to ESPHome device via BLE."""
        # This method interfaces with ESPHome BLE proxy
        # In a real implementation, this would:
        # 1. Get the ESPHome device from the registry
        # 2. Send BLE commands through ESPHome's BLE proxy
        # 3. Format commands according to Neewer protocol

        _LOGGER.debug(
            "Sending command: power=%s, brightness=%s, rgb=%s, color_temp=%s",
            self._attr_is_on,
            self._attr_brightness,
            self._attr_rgb_color,
            self._attr_color_temp,
        )

        # Placeholder for actual BLE communication through ESPHome
        # The actual implementation would use the ESPHome API:
        # - Call esphome API to send BLE write commands
        # - Format data according to Neewer TL60/TL120C protocol
        # - Handle responses and update state
        pass

    async def async_update(self) -> None:
        """Fetch new state data for the light."""
        # In a real implementation, this would query the device state
        # through ESPHome BLE proxy
        pass
