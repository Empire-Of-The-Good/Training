from aiogram import Bot, Dispatcher, types, executor
bot = Bot("")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def SendMessage(message: types.Message):
    await message.answer('Здравствуйте! Ведите сообщение которым вы хотите за спамить')
    word = message.text
executor.start_polling(dp)