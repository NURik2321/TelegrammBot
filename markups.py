from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btnProfile = KeyboardButton("ПРОФИЛЬ")
btnPrepod = KeyboardButton("Поиск препода")

notreg = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile)
mainMenu.add(btnPrepod)

