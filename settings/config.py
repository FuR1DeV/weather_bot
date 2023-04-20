import os
from dotenv import load_dotenv
from emoji import emojize

load_dotenv()

VERSION = '1.0'
AUTHOR = 'Vasiliy Turtugeshev'

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

KEYBOARD = {
    'GRINNING_CAT': emojize(':grinning_cat:'),
    'WEARY_CAT': emojize(':weary_cat:'),
    'DOLLAR_BANKNOTE': emojize(':dollar_banknote:'),
    'MONEY_BAG': emojize(':money_bag:'),
    'SUN': emojize(':sun:'),
    'EXCLAMATION_QUESTION_MARK': emojize(':exclamation_question_mark:'),
    'CLOUD_WITH_LIGHTNING_AND_RAIN': emojize(':cloud_with_lightning_and_rain:'),
    'RIGHT_ARROW_CURVING_LEFT': emojize(':right_arrow_curving_left:'),
}
