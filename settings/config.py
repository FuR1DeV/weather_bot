import os
from dotenv import load_dotenv
from emoji import emojize

load_dotenv()

VERSION = '1.0'
AUTHOR = 'Vasiliy Turtugeshev'


BOT_TOKEN = os.getenv('BOT_TOKEN')


KEYBOARD = {
    "FAST_FORWARD_BUTTON": emojize(':fast-forward_button:'),
    "FAST_REVERSE_BUTTON": emojize(':fast_reverse_button:'),
    'INFORMATION': emojize(':information:'),
    'RIGHT_ARROW_CURVING_LEFT': emojize(':right_arrow_curving_left:'),
}
