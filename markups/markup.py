from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


#  Класс использую для удобства распределения разных клавиатур
class MainMarkup:

    @staticmethod
    def main_markup() -> InlineKeyboardMarkup:
        main = InlineKeyboardMarkup(row_width=2)
        weather = InlineKeyboardButton(text=f'{KEYBOARD.get("SUN")} Узнать погоду '
                                            f'{KEYBOARD.get("CLOUD_WITH_LIGHTNING_AND_RAIN")}',
                                       callback_data='user_check_weather')
        currency = InlineKeyboardButton(text=f'{KEYBOARD.get("DOLLAR_BANKNOTE")} Конвертер валют '
                                             f'{KEYBOARD.get("MONEY_BAG")}',
                                        callback_data='user_currency_converter')
        animals = InlineKeyboardButton(text=f'{KEYBOARD.get("GRINNING_CAT")} Показать милого пушистика '
                                            f'{KEYBOARD.get("WEARY_CAT")}',
                                       callback_data='user_watching_animals')
        poll = InlineKeyboardButton(text=f'{KEYBOARD.get("EXCLAMATION_QUESTION_MARK")} Создать опрос '
                                         f'{KEYBOARD.get("EXCLAMATION_QUESTION_MARK")}',
                                    callback_data='user_create_poll')
        main.insert(weather)
        main.insert(currency)
        main.insert(animals)
        main.insert(poll)
        return main

    @staticmethod
    def back_markup() -> InlineKeyboardMarkup:
        main = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Вернуться в главное меню '
                                         f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")}',
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
        back = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Вернуться в главное меню '
                                         f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")}',
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
        back = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад '
                                         f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} ',
                                    callback_data='user_currency_converter')
        main.insert(back)
        return main


class CreatePolls:

    @staticmethod
    def back_or_finish() -> InlineKeyboardMarkup:
        main = InlineKeyboardMarkup(row_width=2)
        back = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} С начала '
                                         f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} ',
                                    callback_data='user_create_poll')
        finish = InlineKeyboardButton(text=f'Отправить',
                                      callback_data='user_finish_poll')
        main.insert(back)
        main.insert(finish)
        return main
