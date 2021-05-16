from gpiozero import Button as GPIOButton
import time

class Button:
  _gpio_button = None
  _debounce_time = 500
  _last_press = 0
  _channel = None


  def __init__(self, name, key, pin):
    self.name = name
    self.key = key
    self._pin = pin

    self._setup()

  def set_relay_channel(self, channel):
    self._channel = channel

  def _pressed(self):
    press_time = self._current_millis()

    if(self._is_outside_of_debounce(press_time)):
      if(self._channel is not None):
        self._channel.toggle()
        self._last_press = press_time

  def _setup(self):
    self._gpio_button = GPIOButton(self._pin)
    self._gpio_button.when_released = self._pressed

  def _is_outside_of_debounce(self, press_time):
    return press_time - self._last_press > self._debounce_time

  def _current_millis(self):
    return round(time.time() * 1000)