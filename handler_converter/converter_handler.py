from aiogram import types
from aiogram.dispatcher import FSMContext
from currency_converter import CurrencyConverter

from bot import bot
from markups import markup
from states import states


#  Использую классы для общей компоновки по типу сущности
class CurrencyConverterHandler:

    #  Когда мы возвращаемся в главное меню мы сбрасываем машину состояний FSM
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
        #  Достаем из колбэка данные, из кнопки которую нажал пользователь
        pairs = callback.data.split("-")[1]
        first = pairs.split("/")[0]
        second = pairs.split("/")[1]
        #  Сохраняем данные в машину состояний
        await state.update_data(first=first, second=second)
        await callback.message.edit_text(f"<i>Вы выбрали пару</i> <b>{pairs}</b>\n"
                                         f"<i>Теперь введите сумму</i>",
                                         reply_markup=markup.ConverterMarkup.back_to_pairs())
        #  Устанавливаем машину состояний в состоянии converter,
        #  чтобы сработала нужная функция
        await states.UserStates.converter.set()

    @staticmethod
    async def currency_result(message: types.Message, state: FSMContext):
        #  Создаем объект класса CurrencyConverter
        currency = CurrencyConverter()
        #  Проверяем данные на валидность введенные пользователем
        if message.text.isdigit():
            user_input = int(message.text)
            #  Число должно быть натуральным
            if user_input > 0:
                #  Берем из машины состояний сохраненные данные
                async with state.proxy() as data:
                    result = round(currency.convert(user_input, data.get("first"), data.get("second")), 2)
                    #  Удаляем введенные данные для красоты
                    await bot.delete_message(message.from_user.id, message.message_id)
                    await bot.delete_message(message.from_user.id, message.message_id - 1)
                    await bot.send_message(message.from_user.id,
                                           f"<i>За</i> <b>{user_input} {data.get('first')}</b> "
                                           f"<i>дают</i> <b>{result} {data.get('second')}</b>",
                                           reply_markup=markup.ConverterMarkup.pairs())
            #  Сбрасываем машину состояний
            await state.finish()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Нужно ввести натуральное число!\n"
                                   f"Введите нужную сумму</b>",
                                   reply_markup=markup.ConverterMarkup.back_to_pairs())
