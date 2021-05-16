import json
import signal

from relay import Relay
from button import Button

def load_config():
  with open('config.json') as f:
    return json.load(f)

# parse config
config = load_config()


# set up relay
relay = Relay()
for val in config['relay']['channels']:
  relay.add_channel(val['name'], val['key'], val['pin'])


# set up buttons
buttons = []
for button_config in config['buttons']:
  button = Button(button_config['name'], button_config['key'], button_config['pin'])
  button.set_relay_channel(relay.get_channel(button_config['key']))

  buttons.append(button)


# todo(chrisjacob): set up RabbitMQ
# set up RabbitMQ

signal.pause()
