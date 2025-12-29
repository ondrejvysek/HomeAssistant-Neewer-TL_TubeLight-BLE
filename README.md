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
- An ESP32 device supported by ESPHome (example: M5Stack Atom)
- Neewer TL tube(s) reachable over BLE

## Installation (ESPHome YAML)

1. Create a new ESPHome device (ESP32) in Home Assistant.
2. Use the example YAML from this repository (or copy the snippet below).
3. Set Wi-Fi secrets in Home Assistant (`wifi_ssid`, `wifi_password`).
4. Set the BLE MAC address(es) of your tube light(s).
5. Compile and flash.

### Example YAML

Use `external_components` so ESPHome pulls the component directly from this GitHub repo:

```yaml
external_components:
  - source:
      type: git
      url: https://github.com/ondrejvysek/HomeAssistant-Neewer-TL_TubeLight-BLE
      ref: main
    components: [neewer_tl_tube_ble]
```

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
