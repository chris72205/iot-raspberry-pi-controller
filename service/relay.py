from gpiozero import LED
import time
import logging

class Channel:
  _pin = None
  _output = None

  _debounce_time = 500
  _last_press = 0

  def __init__(self, name, pin):
    self.name = name
    self.pin = pin

    self._output = LED(pin)

  def get_state(self):
    self._output.is_active

  def turn_on(self):
    if(not self.safety_enabled() and self._is_outside_of_debounce(self._current_millis())):
      self._last_press = self._current_millis()
      self._output.on()

  def turn_off(self):
    # no debounce here, we can always turn it off
    self._output.off()

  def toggle(self):
    if(not self.safety_enabled() and self._is_outside_of_debounce(self._current_millis())):
      self._last_press = self._current_millis()
      self._output.toggle()

  def _is_outside_of_debounce(self, press_time):
    return press_time - self._last_press > self._debounce_time

  def _current_millis(self):
    return round(time.time() * 1000)

    def _safety_enabled(self):
      # todo(chrisjacob): return true if channel has changed state more than _x_ times in _n_ seconds

class Relay:
  _channels = {}

  def add_channel(self, name, key, pin):
    self._channels[key] = Channel(name, pin)

  def get_channel(self, key):
    return self._channels[key]

  def turn_on(self, key):
    if(self._channels.has_key(key)):
      self._channels[key].turn_on()

  def turn_off(self, key):
    if(self._channels.has_key(key)):
      self._channels[key].turn_off()

  def toggle(self, key):
    if(self._channels.has_key(key)):
      self._channels[key].toggle()
