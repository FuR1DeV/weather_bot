from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from handler_weather import register_weather_handler
from handler_converter import register_currency_converter_handler
from handler_animals import nice_animals
from settings import config
from markups import markup


@dp.message_handler(commands='start', state='*')
async def start(message: types.Message):
    await message.answer(
        '<b>Это тестовое задание для ИП Богданов Денис Александрович</b>',
        reply_markup=markup.MainMarkup.main_markup())


async def on_startup(_):
    register_weather_handler(dp)
    register_currency_converter_handler(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
