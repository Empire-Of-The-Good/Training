from aiogram import Bot, Dispatcher, types, executor
bot = Bot('')
po = Dispatcher(bot)

@po.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Ку')

if __name__ == '__main__':
    executor.start_polling(po, skip_updates=True)