"""Constants for the Neewer Tube Light integration."""

DOMAIN = "neewer_light"

# Supported models
MODEL_TL60_RGB = "TL60 RGB"
MODEL_TL120C = "TL120C"

SUPPORTED_MODELS = [MODEL_TL60_RGB, MODEL_TL120C]

# Configuration
CONF_ESPHOME_DEVICE = "esphome_device"

# Default values
DEFAULT_NAME = "Neewer Tube Light"

# Color temperature range (in mireds)
MIN_MIREDS = 153  # ~6500K
MAX_MIREDS = 370  # ~2700K

# BLE Service and Characteristic UUIDs (placeholders - adjust based on actual device)
SERVICE_UUID = "69400001-b5a3-f393-e0a9-e50e24dcca99"
CHARACTERISTIC_UUID_CONTROL = "69400002-b5a3-f393-e0a9-e50e24dcca99"
CHARACTERISTIC_UUID_STATUS = "69400003-b5a3-f393-e0a9-e50e24dcca99"
