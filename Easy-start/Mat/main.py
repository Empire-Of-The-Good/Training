from aiogram import Bot, Dispatcher, types, executor
import os, json, string
bot = Bot('ApI')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Ку')
    
@dp.message_handler(content_types=['text'])
async def mats(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open("mat.json")))) != set():
            await message.reply('Это слово запрщено!')
            await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)