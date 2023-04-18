from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from currency_converter import currency_converter
from nice_animals import nice_animals
from settings import config
from markups import markup


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer(
        'Это тестовое задание для ИП Богданов Денис Александрович',
        reply_markup=markup.UserMainMarkup.main_markup())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
