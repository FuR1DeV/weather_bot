from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    weather: State = State()
    converter: State = State()
