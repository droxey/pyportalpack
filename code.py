'''
code.py
---
Customize this file to write your own PyPortal applications.
'''

import time
import board

import config
from adafruit_pyportal import PyPortal


# Initialize the PyPortal using settings from the config.py file.
pyportal = PyPortal(url=config.DATA_SOURCE,
                    json_path=(config.QUOTE_LOCATION, config.AUTHOR_LOCATION),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=config.BG_IMAGE,
                    text_font=config.FONT,
                    debug=config.DEBUG,
                    text_position=config.TEXT_POSITION,
                    text_color=config.TEXT_COLORS,
                    text_wrap=config.TEXT_WRAP,
                    text_maxlen=config.TEXT_MAX_LENGTH)

# Speed up projects with lots of text by preloading the font!
pyportal.preload_font()

# Run the code in an infinite loop.
while True:
    try:
        # Refresh the screen!
        value = pyportal.fetch()
        print("Response is", value)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(0)
