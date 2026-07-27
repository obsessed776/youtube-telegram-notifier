import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import config


if not config.TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(f"Hello <b>{message.from_user.first_name}</b>!")


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
