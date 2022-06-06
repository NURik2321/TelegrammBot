from aiogram import Bot,Dispatcher,executor,types
import config
import markups
from db import Database

bot = Bot(config.TOKEN)

db = Database('database.db')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message : types.Message):
        if(not db.user_check(message.from_user.id)):
                db.add_user(message.from_user.id)
                await bot.send_message(message.from_user.id, "Укажите ваш ник")
        else:
                await bot.send_message(message.from_user.id , "Вы уже зарегистрированы",reply_markup=markups.mainMenu)

@dp.message_handler()
async def bot_message(message : types.Message):
        if message.chat.type == 'private':
                if(message.text == "ПРОФИЛЬ"):
                        pass
                else:
                        if(db.get_signup(message.from_user.id) == "setnickname"):
                                if(len(message.text) >15):
                                        await bot.send_message(message.from_user.id, "Ник слишком большой")
                                elif '@' in message.text or '/' in message.text:
                                        await bot.send_message(message.from_user.id, "Вот енто @ и / нельзя")
                                else:
                                        db.set_nickname(message.from_user.id,message.text)
                                        db.set_signup(message.from_user.id, "done")
                                        await bot.send_message(message.from_user.id, "Ура вы зареганы!!",reply_markup=markups.mainMenu)
                        else:
                                await bot.send_message(message.from_user.id, "Больше нечего не умею")




if (__name__=="__main__"):
        executor.start_polling(dp,skip_updates=True)