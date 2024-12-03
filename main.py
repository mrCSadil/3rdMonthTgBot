from aiogram import types, executor
from config import bot, dp
import logging
import os


@dp.message_handler(commands=["start", "help"])
async def start_handler(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}!\n"
                           f"Your telegram id - {message.from_user.id}\n")

@dp.message_handler(commands=["BUBUBU"])
async def meme_handler(message:types.Message):
    photo_pass = os.path.join("media", "hqdefault.jpg")
    with open(photo_pass, "rb") as photo:
        await message.answer_photo(photo = photo, caption= "BUBUBU, I can't see, BUBUBU")

@dp.message_handler(commands=["crocodile"])
async def meme_handler(message:types.Message):
    photo_pass = os.path.join("media", "img.png")
    with open(photo_pass, "rb") as photo:
        await message.answer_photo(photo = photo, caption= "crocodile")

@dp.message_handler()
async def echo_message(message:types.Message):
    text = message.text
    if text.isdigit():
        squared = int(text)**2
        await bot.send_message(message.chat.id, squared)
    else:
        await bot.send_message(message.chat.id, text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)