from aiogram import Bot, Dispatcher, types, executor
from sqlite import db_start, create_profile, edit
bot = Bot('')
po = Dispatcher(bot)

async def lol(_):
    await db_start()

@po.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Ку')
    await create_profile(user_id=message.from_user.id)

if __name__ == '__main__':
    executor.start_polling(po, skip_updates=True, on_startup=lol)