from aiogram import Bot, Dispatcher, types, executor
from translate import Translator 
bot = Bot("")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def Send(message: types.Message):
    await message.answer('Здравствуйте! Ведите сообщение  ')

ru_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en_letters = "abcdefghijklmnopqrstuvwxyz"


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, вебери с какого языка на каой переводить, пока доступно только 2 языка русскиий английский:(\
                        Например напиши рус/англ тогда ты выберешь переводить с русского на английский\
                        А если хочешь  переводить наоборот с английского на русский напиши англ/рус")


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    text = message.text
    if text == 'рус/англ':
        if text[0].lower() in ru_letters:
          translator = Translator(from_lang="russian", to_lang="english")
        elif text[0].lower() in en_letters:
            translator = Translator(from_lang="english", to_lang="russian")
        else:
            await message.answer('Я тебя не понимаю')
            return
    
    
    translation = translator.translate(text)
    await message.answer(translation)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
