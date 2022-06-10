from aiogram import Bot,Dispatcher,executor,types
import config
import markups
from db import DatabaseREg
from dbprepod import DatabasePropod
bot = Bot(config.TOKEN)

db = DatabaseREg('database.db')
dbprepod = DatabasePropod('database.db')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message : types.Message):
        if(not db.user_check(message.from_user.id)):
                db.add_user(message.from_user.id)
                await bot.send_message(message.from_user.id,"/reg" , reply_markup=markups.notreg)
                await bot.send_message(message.from_user.id, "Укажите ваш ник")

        else:
                await bot.send_message(message.from_user.id , "Вы уже зарегистрированы",reply_markup=markups.mainMenu)

@dp.message_handler()
async def bot_message(message : types.Message):
        if message.chat.type == 'private':
                if(message.text == "ПРОФИЛЬ"):
                        await bot.send_message(message.from_user.id, " Ваш email "+db.get_email(message.from_user.id))


                elif(dbprepod.getPrepod(message.text) != None):
                      await bot.send_message(message.from_user.id,dbprepod.getPrepod(message.text))

                elif(message.text == "Поиск препода"):
                        await bot.send_message(message.from_user.id, "Для того чтобы найти информацию введите фамилию и инициалы ")

                else:

                        if(db.get_signup(message.from_user.id) == "setnickname"):
                                if(len(message.text) >15):
                                        await bot.send_message(message.from_user.id, "Ник слишком большой")
                                elif '@' in message.text or '/' in message.text:
                                        await bot.send_message(message.from_user.id, "Вот енто @ и / нельзя")
                                else:
                                        db.set_nickname(message.from_user.id,message.text)
                                        await bot.send_message(message.from_user.id, "Укажите Email")
                                        db.set_signup(message.from_user.id, "setemail")
                        elif(db.get_signup(message.from_user.id)=="setemail"):

                                if(message.text.find("@") == -1):
                                        await bot.send_message(message.from_user.id, "email указан не верно")
                                else:

                                        db.set_email(message.from_user.id,message.text)
                                        await bot.send_message(message.from_user.id, "Укажите пороль")
                                        db.set_signup(message.from_user.id, "setpassword")
                        elif (db.get_signup(message.from_user.id) == "setpassword"):

                                db.set_password(message.from_user.id, message.text)
                                await bot.send_message(message.from_user.id, "Вы успешно прошли регистрацию" ,reply_markup=markups.mainMenu)
                                db.set_signup(message.from_user.id, "done")


                        else:
                                await bot.send_message(message.from_user.id, "Больше нечего не умею")




if (__name__=="__main__"):
        executor.start_polling(dp,skip_updates=True)