import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config


if not config.TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

dp = Dispatcher()


class AddSubscriptionState(StatesGroup):
    youtube_channel = State()
    telegram_chat = State()


# TODO: add callback query
def build_channel_input_data_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="by URL")
    keyboard.button(text="by handle")
    keyboard.button(text="by ID")
    return keyboard.as_markup()


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(f"Hello <b>{message.from_user.first_name}</b>!")


@dp.message(Command("add"))
async def start_add_subscription_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(AddSubscriptionState.youtube_channel)
    await message.answer("Choose the method we will use to search for the YouTube channel.",
                         reply_markup=build_channel_input_data_keyboard())


@dp.message(AddSubscriptionState.youtube_channel, F.text)
async def process_youtube_channel(message: Message, state: FSMContext) -> None:
    pass


async def process_telegram_chat(message: Message, state: FSMContext) -> None:
    pass


@dp.message(AddSubscriptionState.youtube_channel)
async def process_youtube_channel_invalid_content_type(message: Message) -> None:
    await message.answer("Sorry, i didn't understand. Send youtube channel id or handle as text.")


async def main() -> None:
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Closing bot ...")
