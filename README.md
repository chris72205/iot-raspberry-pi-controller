# iot-raspberry-pi-controller

Control relay(s) with a Raspberry Pi.  Should run as a system service and update the relay state(s) based on messages via MQTT/AMQP or physical momentary switch(es).

## Setup

### Configuration

Place populated `config.json` next to `main.py` with configured values.  See `config.sample.json` for what this should look like.

### System service

Copy `iot-raspberry-pi-controller.service` to `/etc/systemd/system` and then run `sudo systemctl start iot-raspberry-pi-controller.service`.  If satisfied, enable it with `sudo systemctl enable iot-raspberry-pi-controller.service`.  The service can be stopped at any time by running `sudo systemctl stop iot-raspberry-pi-controller.service`.

## Todo

- set up messaging via RabbitMQ
  - consume messages to toggle relay channels
  - publish messages with latest status of relay channels
- add output logging of switch state changes and around RabbitMQ messages
- look into how to properly package this for easier installation/deployment (thinking about installing python dependencies)
- tests??