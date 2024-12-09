from aiogram import executor
from config import bot, dp, Admins
import logging
from handlers import commands, echo, quiz

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin , text= "Bot was activated")

async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin , text= "Bot was deactivated")

commands.register_commands_handlers(dp)
quiz.register_quiz_handlers(dp)
echo.register_echo_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)