# Nanpy

[![Latest Version](https://pypip.in/version/nanpy/badge.svg)](https://pypi.python.org/pypi/nanpy/)
[![Travis](http://img.shields.io/travis/nanpy/nanpy.svg)] (https://travis-ci.org/nanpy/nanpy)
[![Coveralls](http://img.shields.io/coveralls/nanpy/nanpy/master.svg)] (https://coveralls.io/r/nanpy/nanpy)
[![Supported Python versions](https://pypip.in/py_versions/nanpy/badge.svg)](https://pypi.python.org/pypi/nanpy/)
[![License](https://pypip.in/license/nanpy/badge.svg)](https://pypi.python.org/pypi/nanpy/)
[![Downloads](https://pypip.in/download/nanpy/badge.svg)](https://pypi.python.org/pypi/nanpy/)

Use your Arduino board with Python. http://pypi.python.org/pypi/nanpy

## Overview

Nanpy is a library that use your Arduino as a slave, controlled by a master device where you run your scripts, such as a PC, a Raspberry Pi etc.
The main purpose of Nanpy is making programmers' life easier, providing them a powerful library to create prototypes faster and make Arduino programming a game for kids.

    a = ArduinoApi()
    a.pinMode(13, a.OUTPUT)
    a.digitalWrite(13, a.HIGH)

I know, there are a lot of projects able to do that, but hey, Nanpy can do more!
Nanpy is easily extensible and can theoretically use every library, allowing you to create how many objects you want.
We support OneWire, Lcd, Stepper, Servo, DallasTemperature and many more...
Let's try to connect our 16x2 lcd screen on pins 7, 8, 9, 10, 11, 12 and show your first "Hello world"!

    from nanpy import Lcd

    lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
    lcd.printString('Hello World!')

really straightforward now, isn't it? :)

### Serial communication

Nanpy autodetects the serial port for you, anyway you can manually specify another serial port:

    from nanpy import SerialManager
    connection = SerialManager(device='/dev/ttyACM1')

and use it with your objects

    a = ArduinoApi(connection=connection)
    a.pinMode(13, a.OUTPUT)
    a.digitalWrite(13, a.HIGH)

You can specify how many SerialManager objects you want and control more than one Arduino board within the same script.

---

## How to build and install

First of all, you need to build the firmware and upload it on your Arduino, to do that clone the [nanpy-firmware repository on Github](https://github.com/nanpy/firmware) or [download it from PyPi](https://pypi.python.org/pypi/nanpy).

    git clone git@github.com:nanpy/nanpy-firmware.git
    cd nanpy-firmware
    ./configure.sh

You can now edit Nanpy/cfg.h generated file to configure your Nanpy firmware, selecting the features you want to include and the baud rate.
To build and install Nanpy firmware, copy Nanpy directory under your "sketchbook" directory, start your Arduino IDE, open Sketchbook -> Nanpy and click on "Upload".

To install Nanpy Python library on your master device just type:

    pip install nanpy

---

## How to contribute

Nanpy still needs a lot of work. You can contribute with patches (bugfixing, improvements, adding support for a new library not included in Nanpy yet, writing examples and so on), writing documentation, reporting bugs, creating packages or simply spreading Nanpy through the web if you like it :) If you have any doubt or problem, please contact me at <stagi.andrea@gmail.com>

Do you want to support us with a coffee? We need a lot of caffeine to code all night long! if you like this project and you want to support us, [please donate using Paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TDTPP5JHVJK8J)

---

## License

This software is released under MIT License. Copyright (c) 2012-2014 Andrea Stagi <stagi.andrea@gmail.com>
