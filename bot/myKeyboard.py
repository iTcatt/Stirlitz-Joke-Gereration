from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)

help_button = KeyboardButton('/help')
gen_button = KeyboardButton('/generate')

kb.add(gen_button).add(help_button)