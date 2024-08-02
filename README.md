# BLE Signal Collector

## Description
BLE Signal Collector is a system designed to capture and log Bluetooth Low Energy (BLE) signal data sent from mobile phones using Raspberry Pi devices. The Raspberry Pi devices receive the BLE signals, log the data, and transmit it to a central server via Wi-Fi for analysis.

## Features
- Collects BLE signal data such as RSSI, MAC address, UUID, and timestamp.
- Supports multiple Raspberry Pi devices with dynamic endpoint handling.
- Stores data in CSV files for easy analysis.
- Utilizes mobile phones to send BLE signals and Raspberry Pi devices to receive and forward the data to the server.

## Requirements
- Node.js
- Express.js
- body-parser
- Raspberry Pi with BLE support (Raspberry Pi 3B+)
- Python (for Raspberry Pi script)
- Wi-Fi network

## Installation

### Server Setup
1. Clone the repository:

2. Install the necessary Node.js packages:
    ```bash
    npm install
    ```
3. Start the server:
    ```bash
    node server.js
    ```

### Raspberry Pi Setup
1. Install the required Python packages:
    ```bash
    pip install requests bluepy
    ```
2. Update the `scan.py` script to match your server IP address:
    ```python
    # scan.py
    r = requests.post('http://<server-ip>:9527/<sniffer_id>', data=my_data)
    ```

## Usage
- Deploy the updated `scan.py` script on each Raspberry Pi device.
- Ensure the Raspberry Pi devices are connected to the Wi-Fi network.
- Start the server using the `node server.js` command.
- Monitor the server logs for incoming data and check the generated CSV files.
