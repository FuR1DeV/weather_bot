__all__ = ["register_create_polls_handler"]

from aiogram import Dispatcher

from .polls import CreatePolls
from states import states


def register_create_polls_handler(disp: Dispatcher) -> None:
    """Create Polls handler"""

    disp.register_callback_query_handler(CreatePolls.create_poll,
                                         state=["*"],
                                         text="user_create_poll")
    disp.register_message_handler(CreatePolls.question,
                                  state=states.UserQuestion.question)
    disp.register_message_handler(CreatePolls.answers,
                                  state=states.UserQuestion.answers)
    disp.register_callback_query_handler(CreatePolls.finish,
                                         state=["*"],
                                         text="user_finish_poll")
