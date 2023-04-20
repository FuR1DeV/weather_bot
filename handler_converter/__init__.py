__all__ = ["register_currency_converter_handler"]

from aiogram import Dispatcher

from .converter_handler import CurrencyConverterHandler
from states import states


def register_currency_converter_handler(disp: Dispatcher) -> None:
    """Currency Converter handler"""

    disp.register_callback_query_handler(CurrencyConverterHandler.enter_currency,
                                         state=["*"],
                                         text="user_currency_converter")
    disp.register_callback_query_handler(CurrencyConverterHandler.currencies_choice,
                                         state=["*"],
                                         text_contains="enter_currency")
    disp.register_message_handler(CurrencyConverterHandler.currency_result,
                                  state=states.UserStates.converter)
