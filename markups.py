from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btnProfile = KeyboardButton("ПРОФИЛЬ")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile)
