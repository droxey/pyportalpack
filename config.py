'''
config.py
---
Change the variables in ALL_CAPS below to customize your own PyPortal programs.
'''

# Current directory (DO NOT CHANGE)
_portaldir = ("/" + __file__).rsplit('/', 1)[0] + "/"

# Background image used at startup:
BG_IMAGE = _portaldir + 'thankyou.bmp'

# Font in BDF format:
FONT = _portaldir + 'fonts/Arial-ItalicMT-17.bdf'

# JSON data source URL:
DATA_SOURCE = "https://www.adafruit.com/api/quotes.php"

# JSON location of the quote and author:
QUOTE_LOCATION = [0, 'text']
AUTHOR_LOCATION = [0, 'author']

# Change text attributes on the screen:
TEXT_POSITION = ((20, 40), (100, 190))
TEXT_COLORS = (0xFFFFFF, 0x8080FF)
TEXT_WRAP = (35, 0)
TEXT_MAX_LENGTH = (170, 30)

# Run in DEBUG mode. True in development, False for releases:
DEBUG = True
