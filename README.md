# HomeAssistant Neewer TL TubeLight BLE Control

This custom component controls Neewer tube lights, tested on TL120C and TL60 RGB

Using ATOM M5 as BLE gateway

This project exposes Neewer TL tube lights over BLE as a native Home Assistant **Light** entity via ESPHome.
You get the standard HA UI, including the **color picker**, brightness slider, and white channel control (CW/WW).

## Features

- On/Off
- Brightness
- RGB color control
- Cold/Warm white control (CW/WW)
- Multiple tubes grouped into a single HA light entity
- Keepalive handling

## Requirements

- Home Assistant with the ESPHome add-on (or ESPHome CLI)
- An ESP32 device supported by ESPHome (example: M5Stack Atom Lite https://shop.m5stack.com/products/atom-lite-esp32-development-kit)
- Neewer TL tube(s) reachable over BLE

## Installation (ESPHome YAML)

1. Create a new ESPHome device (ESP32) in Home Assistant.
2. Use the example YAML from this repository (or copy the snippet below).
3. Set Wi-Fi secrets in Home Assistant (`wifi_ssid`, `wifi_password`).
4. Set the BLE MAC address(es) of your tube light(s).
5. Compile and flash.

### Example YAML

Recommended max number of the BLE devices is 3

```yaml
# neewer-atom-sample.yaml
substitutions:
  name: neewer-atom-ble
  friendly_name: Neewer Atom BLE

  # Neewer BLE GATT (from your sniff)
  neewer_service_uuid: "69400001-B5A3-F393-E0A9-E50E24DCCA99"
  neewer_char_uuid_cmd: "69400002-B5A3-F393-E0A9-E50E24DCCA99"

esphome:
  name: ${name}
  friendly_name: ${friendly_name}

esp32:
  board: m5stack-atom
  framework:
    type: arduino

logger:
  level: DEBUG

api:

ota:
  - platform: esphome

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  ap:
    ssid: "${friendly_name} Fallback"
    password: "12345678"

captive_portal:
web_server:

esp32_ble_tracker:
  scan_parameters:
    active: true
    interval: 1100ms
    window: 1100ms

# Remote packages from GitHub (same file can be included multiple times with different vars)
# This is the correct way to reference a GitHub YAML file (no /config/esphome/... local path).
packages:
  neewer_tubes:
    url: https://github.com/ondrejvysek/HomeAssistant-Neewer-TL_TubeLight-BLE
    ref: main
    files:
      - path: components/neewer_atom_tube/neewer_atom_tube.yaml
        vars:
          dev_id: tube1
          dev_name: "Tube 1"
          dev_mac: "XX:XX:XX:XX:XX:XX"
          service_uuid: ${neewer_service_uuid}
          char_uuid: ${neewer_char_uuid_cmd}

      - path: components/neewer_atom_tube/neewer_atom_tube.yaml
        vars:
          dev_id: tube2
          dev_name: "Tube 2"
          dev_mac: "XX:XX:XX:XX:XX:XX"
          service_uuid: ${neewer_service_uuid}
          char_uuid: ${neewer_char_uuid_cmd}

      - path: components/neewer_atom_tube/neewer_atom_tube.yaml
        vars:
          dev_id: tube3
          dev_name: "Tube 3"
          dev_mac: "XX:XX:XX:XX:XX:XX"
          service_uuid: ${neewer_service_uuid}
          char_uuid: ${neewer_char_uuid_cmd}
```
### Control all lights together

Create HomeAssistant group (https://www.home-assistant.io/integrations/group/)
- Browse to your Home Assistant instance.
- Go to  Settings > Devices & Services.
- At the top of the screen, select the tab: Helpers.
- In the bottom right corner, select the  Create helper button.
- From the list, select Group.
- Follow the instructions on screen to complete the setup.

## Finding the BLE MAC address (BLE Scanner)

You need the tube’s BLE MAC address for the ble_client configuration.

### Option A: Use the “BLE Scanner” phone app (recommended)

Install BLE Scanner on an Android phone.

Enable Bluetooth and Location (Android requires location permission for BLE scanning).

Scan for nearby BLE devices.

Find your Neewer tube (by name if advertised, or by RSSI proximity).

Copy the MAC address (format like F7:67:78:20:CB:E8).

Note:

On iOS/macOS, BLE APIs often show a UUID-like identifier instead of the real MAC address due to privacy restrictions. If you don’t see a MAC, use Android or the ESPHome log method below. (CoreBluetooth commonly identifies peripherals by UUID rather than Bluetooth address.)

### Option B: Use ESPHome logs (no phone apps)

Temporarily enable esp32_ble_tracker: in your ESPHome device.

Open ESPHome logs in Home Assistant.

Look for discovered BLE devices and their addresses.

Copy the address for your tube.

Adding more tubes

Add more ble_client entries and include them under tubes::


## Disclaimer

This is a community project. No affiliation with Neewer.
