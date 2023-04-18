import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import bot
from markups import markup
from states import states
from settings import config


class WeatherHandler:

    #  Когда мы возвращаемся в главное меню мы сбрасываем машину состояний FSM
    @staticmethod
    async def main_menu(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text(
            "<b>Это тестовое задание для ИП Богданов Денис Александрович</b>",
            reply_markup=markup.MainMarkup.main_markup())
        await state.finish()

    @staticmethod
    async def weather_enter_city(callback: types.CallbackQuery):
        await callback.message.edit_text("<b>Введите город</b>",
                                         reply_markup=markup.MainMarkup.back_markup())
        #  Устанавливаем машину состояний в состоянии converter,
        #  чтобы сработала нужная функция
        await states.UserStates.weather.set()

    @staticmethod
    async def weather_info(message: types.Message):
        city = message.text
        try:
            #  Парсим данные из бесплатной API
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.WEATHER_TOKEN}&units=metric"
            )
            data = r.json()
            #  Если город не найден, то мы это сообщаем пользователю
            if data.get("cod") == "404":
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.send_message(message.from_user.id,
                                       f"<b>Город {city} не найден!</b>\n"
                                       f"<b>Введите другой город</b>",
                                       reply_markup=markup.MainMarkup.back_markup())
            else:
                #  Если город найден выводим пользователю данные
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.send_message(message.from_user.id,
                                       f"В городе - <b>{city}</b>\n"
                                       f"Температура: <b>{data.get('main').get('temp')} градусов цельсия</b>\n"
                                       f"Ощущается как: <b>{data.get('main').get('feels_like')} градусов цельсия</b>\n"
                                       f"Давление: <b>{data.get('main').get('pressure')} мм. рт. ст.</b>",
                                       reply_markup=markup.MainMarkup.back_markup())
        #  На случай если произошло что то непредвиденное (сервер не отвечает)
        except Exception as ex:
            await bot.send_message(message.from_user.id,
                                   f"<b>Что то пошло не так!</b>\n"
                                   f"Ошибка - {ex}",
                                   reply_markup=markup.MainMarkup.back_markup())


