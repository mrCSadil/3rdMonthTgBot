from aiogram import types , Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import random

async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)

    button = InlineKeyboardButton("Далее", callback_data="quiz_2")

    keyboard.add(button)

    question = "XBOX or SONY"
    answer = ["XBOX", "SONY", "Nintendo"]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type = "quiz",
        correct_option_id=1,
        explanation="no explanation",
        open_period=60,
        reply_markup=keyboard,
    )

async def quiz_2(call: types.CallbackQuery):

    question = "PHP, JavaScript, Java , Python and Swift"
    answer = ["PHP", "JavaScript", "Java", "Python", "Swift"]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type = "quiz",
        correct_option_id=3,
        explanation="NO explanation",
        open_period=30,
    )


async def dice(call: types.CallbackQuery):
    dice_emoji = random.choice(["⚽", "🎰", "🏀", "🎯", "🎳", "🎲"])
    await bot.send_dice(chat_id=call.from_user.id, emoji=dice_emoji)


def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, text="quiz_2")
    dp.register_message_handler(dice, commands=["dice"])