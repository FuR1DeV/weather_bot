from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


#  Класс использую для удобства распределения разных клавиатур
class MainMarkup:

    @staticmethod
    def main_markup() -> InlineKeyboardMarkup:
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
    def back_markup() -> InlineKeyboardMarkup:
        main = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(text='Вернуться в главное меню',
                                    callback_data='user_back_in_menu')
        main.insert(back)
        return main


class ConverterMarkup:

    @staticmethod
    def pairs() -> InlineKeyboardMarkup:
        main = InlineKeyboardMarkup(row_width=3)
        usd_eur = InlineKeyboardButton(text='USD/EUR',
                                       callback_data=f'enter_currency-USD/EUR')
        eur_usd = InlineKeyboardButton(text='EUR/USD',
                                       callback_data='enter_currency-EUR/USD')
        gbr_eur = InlineKeyboardButton(text='GBP/EUR',
                                       callback_data='enter_currency-GBP/EUR')
        eur_gbr = InlineKeyboardButton(text='EUR/GBP',
                                       callback_data='enter_currency-EUR/GBP')
        gbr_usd = InlineKeyboardButton(text='GBP/USD',
                                       callback_data='enter_currency-GBP/USD')
        usd_gbr = InlineKeyboardButton(text='USD/GBP',
                                       callback_data='enter_currency-USD/GBP')
        back = InlineKeyboardButton(text='Вернуться в главное меню',
                                    callback_data='user_back_in_menu')
        main.insert(usd_eur)
        main.insert(eur_usd)
        main.insert(gbr_eur)
        main.insert(eur_gbr)
        main.insert(gbr_usd)
        main.insert(usd_gbr)
        main.insert(back)
        return main

    @staticmethod
    def back_to_pairs() -> InlineKeyboardMarkup:
        main = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(text='Назад',
                                    callback_data='user_currency_converter')
        main.insert(back)
        return main
