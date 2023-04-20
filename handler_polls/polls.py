from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import bot
from markups import markup
from states import states


#  Использую классы для общей компоновки по типу сущности
class CreatePolls:

    @staticmethod
    async def create_poll(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите Вопрос:",
                                         reply_markup=markup.MainMarkup.back_markup())
        await states.UserQuestion.question.set()

    @staticmethod
    async def question(message: types.Message, state: FSMContext):
        question = message.text
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        #  Создаем в памяти необходимые переменные чтобы потом с ними взаимодействовать
        await state.update_data(question=question, answers=[], text=[])
        await bot.send_message(message.from_user.id,
                               "<b>Ваш вопрос</b>\n\n"
                               f"<i>{question}</i>\n\n"
                               f"<b>Теперь введите варианты ответов:</b>",
                               reply_markup=markup.MainMarkup.back_markup())
        await states.UserQuestion.answers.set()

    @staticmethod
    async def answers(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            #  Достаём из памяти вопрос и список ответов
            question = data.get("question")
            answers = data.get("answers")
            #  Записываем текущий ответ в список ответов
            answers.append(message.text)
            #  Обновляем в памяти список ответов
            data["answers"] = answers
            #  Тут мы начинаем формировать красивый список текста, так чтобы пользователь
            #  видел какие ответы он писал ранее
            text = data.get("text")
            text.append(f"<b>Ответ №{len(answers)}</b> - <i>{message.text}</i>\n")
            #  Далее обновляем список состоящий из текста
            data["text"] = text
        await bot.send_message(message.from_user.id,
                               "<b>Ваш вопрос</b>\n\n"
                               f"<i>{question}</i>\n\n"
                               #  Тут мы список текста формируем в строку
                               f"{''.join(text)}\n"
                               "<b>Введите следующий вариант ответа или нажмите Отправить:</b>",
                               reply_markup=markup.CreatePolls.back_or_finish())

    #  С помощью send_poll отправляем опрос в любую группу
    #  Групповой чат написал свой, из прошлых проектов @FlowWorkDeliveryHelp.
    #  Можно много вариантов опроса сделать, подставлять chat_id, куда хочешь скинуть опрос.
    @staticmethod
    async def finish(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            answers = data.get("answers")
            question = data.get("question")
            await bot.send_poll(chat_id="@FlowWorkDeliveryHelp",
                                question=question,
                                options=answers,
                                is_anonymous=False)
        await callback.message.edit_text("Опрос в чат отправлен!",
                                         reply_markup=markup.MainMarkup.main_markup())
        await state.finish()
