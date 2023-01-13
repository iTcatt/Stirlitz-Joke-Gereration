import logging

from aiogram import Bot, Dispatcher, executor, types

from client import generation

from myKeyboard import kb
from config import TOKEN_API
from commandMessages import(
    START_MESSAGE,
    HELP_COMMAND_MESSAGE,
    ERROR_MESSAGE,
    WAIT_MESSAGE,
)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message) -> None:
    await message.answer(START_MESSAGE, reply_markup=kb)
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHNzVjv9Yl3MqRRvuYHNVJVNsFIFsijAACKQADgfkiAvMTdspYb9oYLQQ')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message) -> None:
    await message.reply(HELP_COMMAND_MESSAGE)


@dp.message_handler(commands=['generate'])
async def send_joke(message: types.Message) -> None:
    await message.answer(text=WAIT_MESSAGE)
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHNzBjv9KicZmGeUfV_lbrwMhMYBFl3QACLQADgfkiAiHGb3nNOpLwLQQ')
    try:
        joke = await generation()
    except KeyboardInterrupt:
        logging.info(" [x] Server is down")
    await message.answer(text=joke)


@dp.message_handler()
async def undefined_behavior(message: types.Message) -> None:
    await message.answer(ERROR_MESSAGE)
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHNbtjvvCCJ13Gv3YFzN2YNAhfVXS9fAACJwADgfkiAll7CHGv2szuLQQ')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  