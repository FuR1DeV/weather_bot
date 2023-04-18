from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class UserMainMarkup:

    @staticmethod
    def main_markup():
        main = InlineKeyboardMarkup(row_width=2)
        weather = InlineKeyboardButton(text='Узнать погоду',
                                       callback_data='user_check_weather')
        currency = InlineKeyboardButton(text='Конвертер валют',
                                        callback_data='user_currency_converter')
        animals = InlineKeyboardButton(text='Показать милого пушистика',
                                       callback_data='user_watching_animals')
        main.insert(weather)
        main.insert(currency)
        main.insert(animals)
        return main
