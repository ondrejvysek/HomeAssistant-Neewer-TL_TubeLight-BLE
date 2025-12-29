# HomeAssistant Neewer Tube Light Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

A HomeAssistant custom component to control Neewer tube lights (TL60 RGB, TL120C) via ESPHome BLE.

## Supported Devices

- **Neewer TL60 RGB**: RGB tube light with brightness control
- **Neewer TL120C**: RGB tube light with brightness and color temperature control

## Prerequisites

- Home Assistant 2023.1 or newer
- ESPHome device with Bluetooth Low Energy (BLE) support (e.g., ESP32)
- ESPHome configured as a BLE proxy

## Installation

### Manual Installation

1. Copy the `custom_components/neewer_light` directory to your HomeAssistant `custom_components` directory
2. Restart Home Assistant

### HACS Installation

1. Add this repository as a custom repository in HACS
2. Search for "Neewer Tube Light" in HACS
3. Install the integration
4. Restart Home Assistant

## Configuration

### Setup via UI

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for "Neewer Tube Light"
4. Enter the following information:
   - **Device Name**: A friendly name for your light
   - **Device ID**: The MAC address of your Neewer light (format: `AA:BB:CC:DD:EE:FF`)
   - **Model**: Select your light model (TL60 RGB or TL120C)
5. Click **Submit**

### ESPHome Configuration

You need an ESP32 device running ESPHome configured as a BLE proxy. Add the following to your ESPHome configuration:

```yaml
esp32:
  board: esp32dev
  framework:
    type: arduino

# Enable Bluetooth
esp32_ble_tracker:
  scan_parameters:
    interval: 1100ms
    window: 1100ms
    active: true

bluetooth_proxy:
  active: true
```

## Usage

Once configured, your Neewer tube light will appear as a light entity in Home Assistant.

### Supported Features

#### TL60 RGB
- Turn on/off
- Brightness control (0-100%)
- RGB color control

#### TL120C
- Turn on/off
- Brightness control (0-100%)
- RGB color control
- Color temperature control (2700K-6500K)

### Automation Example

```yaml
automation:
  - alias: "Turn on Neewer light at sunset"
    trigger:
      platform: sun
      event: sunset
    action:
      service: light.turn_on
      target:
        entity_id: light.neewer_tube_light
      data:
        brightness: 200
        rgb_color: [255, 200, 100]
```

### Service Call Examples

**Turn on with RGB color:**
```yaml
service: light.turn_on
target:
  entity_id: light.neewer_tube_light
data:
  brightness: 255
  rgb_color: [255, 0, 0]  # Red
```

**Turn on with color temperature (TL120C only):**
```yaml
service: light.turn_on
target:
  entity_id: light.neewer_tube_light
data:
  brightness: 200
  color_temp: 250  # Warm white
```

## Troubleshooting

### Light not responding

1. **Check ESPHome device**: Ensure your ESPHome device is online and functioning as a BLE proxy
2. **Check Bluetooth range**: Move the ESP32 closer to the Neewer light
3. **Verify MAC address**: Double-check the device MAC address in the configuration
4. **Check logs**: Look at Home Assistant logs for error messages

### Finding the MAC address

1. Use the ESPHome BLE tracker to scan for devices
2. Use a Bluetooth scanning app on your phone (e.g., nRF Connect)
3. The Neewer lights typically advertise with a name like "NEEWER-XXXX"

### Enable debug logging

Add to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.neewer_light: debug
```

## Development

### Project Structure

```
custom_components/neewer_light/
├── __init__.py          # Component initialization
├── config_flow.py       # Configuration flow
├── const.py            # Constants
├── light.py            # Light platform
├── manifest.json       # Integration manifest
└── strings.json        # Translations
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Technical Details

### BLE Protocol

The Neewer tube lights use Bluetooth Low Energy (BLE) for communication. This integration uses ESPHome's BLE proxy feature to communicate with the lights from Home Assistant.

### Communication Flow

1. Home Assistant → ESPHome device (via API)
2. ESPHome device → Neewer light (via BLE)
3. Light state updates propagate back through the same path

## License

This project is open source. See LICENSE file for details.

## Credits

- Created by [@ondrejvysek](https://github.com/ondrejvysek)
- Inspired by other Neewer light control projects

## Support

For issues, questions, or suggestions:
- Open an issue on [GitHub](https://github.com/ondrejvysek/HomeAssistant-Neewer-TL_TubeLight-BLE/issues)

## Disclaimer

This is an unofficial integration and is not affiliated with or endorsed by Neewer.