import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from currency_converter import CurrencyConverter

from bot import bot
from markups import markup
from states import states
from settings import config


class CurrencyConverterHandler:

    @staticmethod
    async def main_menu(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text(
            "<b>Это тестовое задание для ИП Богданов Денис Александрович</b>",
            reply_markup=markup.MainMarkup.main_markup())
        await state.finish()

    @staticmethod
    async def enter_currency(callback: types.CallbackQuery):
        await callback.message.edit_text("<i>Выберите пары которые хотите конвертировать</i>",
                                         reply_markup=markup.ConverterMarkup.pairs())

    @staticmethod
    async def currencies_choice(callback: types.CallbackQuery, state: FSMContext):
        pairs = callback.data.split("-")[1]
        first = pairs.split("/")[0]
        second = pairs.split("/")[1]
        await state.update_data(first=first, second=second)
        await callback.message.edit_text(f"<i>Вы выбрали пару</i> <b>{pairs}</b>\n"
                                         f"<i>Теперь введите сумму</i>",
                                         reply_markup=markup.ConverterMarkup.back_to_pairs())
        await states.UserStates.converter.set()

    @staticmethod
    async def currency_result(message: types.Message, state: FSMContext):
        currency = CurrencyConverter()
        if message.text.isdigit():
            user_input = int(message.text)
            if user_input >= 0:
                async with state.proxy() as data:
                    # r = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={config.CURRENCY_TOKEN}")
                    # result = r.json()
                    result = round(currency.convert(user_input, data.get("first"), data.get("second")), 2)
                    await bot.delete_message(message.from_user.id, message.message_id)
                    await bot.delete_message(message.from_user.id, message.message_id - 1)
                    await bot.send_message(message.from_user.id,
                                           f"<i>За</i> <b>{user_input} {data.get('first')}</b> "
                                           f"<i>дают</i> <b>{result} {data.get('second')}</b>",
                                           reply_markup=markup.ConverterMarkup.pairs())
        await state.finish()
