import flicklib
import time
import requests
import signal

sleep_time = 0.2

host = 'http://192.168.0.10'
port = '8080'
path = 'volume_adjust'

some_value = 5000
prev_air_wheel_value = None

@flicklib.airwheel()
def spinny(delta):
    global prev_air_wheel_value
    global some_value
    global airwheelvalue

    some_value += delta
    airwheelvalue = int(some_value/100)

    prev_air_wheel_value = airwheelvalue

@flicklib.tap()
def tap(position):
    global taptxt
    taptxt = position

def handle_change(prev, curr):
  if prev and prev != curr:
    if prev > curr:
      r = requests.get(host + ':' + port + '/' + path + '/' + 'down')
    else:
      r = requests.get(host + ':' + port + '/' + path + '/' + 'up')

def main():
  global airwheelvalue

  prev_air_wheel_value = None

  doubletaptxt = ''
  airwheelvalue = None

  # signal.pause()

  while True:
    time.sleep(sleep_time)

    if airwheelvalue:
      handle_change(prev_air_wheel_value, airwheelvalue)
      prev_air_wheel_value = airwheelvalue


if __name__ == '__main__':
  main()
