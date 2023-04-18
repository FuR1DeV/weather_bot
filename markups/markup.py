from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


#  Класс использую для удобства распределения разных клавиатур
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

    @staticmethod
    def back_markup():
        main = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(text='Вернуться в главное меню',
                                    callback_data='user_back_in_menu')
        main.insert(back)
        return main
