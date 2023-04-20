from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    weather: State = State()
    converter: State = State()


class UserQuestion(StatesGroup):
    question: State = State()
    answers: State = State()
