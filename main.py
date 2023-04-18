import requests
from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from handler_weather import register_weather_handler
from handler_converter import register_currency_converter_handler
from settings import config
from markups import markup


@dp.message_handler(commands='start', state='*')
async def start(message: types.Message):
    await message.answer(
        '<b>Это тестовое задание для ИП Богданов Денис Александрович</b>',
        reply_markup=markup.MainMarkup.main_markup())


@dp.callback_query_handler(text="user_watching_animals", state="*")
async def animals(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    r = requests.get(url="https://api.thecatapi.com/v1/images/search")
    animal = r.json()
    await bot.send_photo(callback.from_user.id,
                         animal[0].get("url"))
    await bot.send_message(callback.from_user.id,
                           '<b>Это тестовое задание для ИП Богданов Денис Александрович</b>',
                           reply_markup=markup.MainMarkup.main_markup())


async def on_startup(_):
    register_weather_handler(dp)
    register_currency_converter_handler(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
