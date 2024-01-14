import os
from aiogram import Bot, Dispatcher, types, executor
from pytube import YouTube
import time
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    time.sleep(3)
    await message.answer('Хелло епты, просто кидай ссылку на видео с ютуба которое нужно скачать я скаю и отправлю тебе, пон?')


@dp.message_handler(content_types=['text'])
async def result(message: types.Message):
    url = message.text
    # Проверяем, что ссылка ведет на YouTube
    if not any(substring in url for substring in ["youtube.com", "youtu.be"]):
        await message.reply("Пожалуйста, отправьте ссылку на YouTube видео.")
        return
    try:
        await message.answer('Теперь подожди видео скачиваеться...')
        yt = YouTube(message.text)
        await bot.send_message(message.chat.id, f"Title: {yt.title}\nViews: {yt.views}\nChannel: {yt.author}\nLink to YouTube channel: {yt.channel_url}")
        video = yt.streams.get_highest_resolution().download()
        await bot.send_video(message.chat.id, types.InputFile(video))
        os.remove(video)
    except:
        await message.answer('Извините произошла ошибка, возможно ')
        os.remove(video)
        return
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)