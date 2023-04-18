__all__ = ["register_weather_handler"]

from aiogram import Dispatcher

from .weather import WeatherHandler
from states import states


def register_weather_handler(disp: Dispatcher) -> None:

    """Weather handler"""

    disp.register_callback_query_handler(WeatherHandler.main_menu,
                                         state=['*'],
                                         text="user_back_in_menu")
    disp.register_callback_query_handler(WeatherHandler.weather_enter_city,
                                         state=["*"],
                                         text="user_check_weather")
    disp.register_message_handler(WeatherHandler.weather_info,
                                  state=states.UserStates.weather)
