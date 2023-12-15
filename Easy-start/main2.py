import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from pytube import YouTube

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = Bot(token="API_BOT")
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Здравствуйте! Что бы скачать видео просто скиньте ссылку на видео!")
    key = types.ReplyKeyboardMarkup(row_width=1)
    key.add(types.KeyboardButton('Главное Меню'))

# Обработчик сообщений с ссылкой на YouTube видео
@dp.message_handler(regexp=r'(https?://[^\s]+)')
async def download_video(message: types.Message):
    url = message.text
    
    # Проверяем, что ссылка ведет на YouTube
    if not any(substring in url for substring in ["youtube.com", "youtu.be"]):
        await message.reply("Пожалуйста, отправьте ссылку на YouTube видео.")
        return
    
    try:
        load = await message.answer('Идет процесс скачивания видео...')
        # Скачиваем видео
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        filename = video.download()
        await bot.edit_message_text(text="Еще 2 секунд...", chat_id=message.chat.id, message_id=load.message_id)
        await asyncio.sleep(2)
        await bot.send_video(message.chat.id, types.InputFile(filename))
        await bot.delete_message(chat_id=message.chat.id, message_id=load.message_id)
    
        await message.answer(f'Вы скачали видео: {url}\n')
        
        # Удаляем временный файл
        os.remove(filename)
    except Exception as e:
        await message.reply("Извините, произошла ошибка при скачивании видео.")

# Запускаем бота
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()