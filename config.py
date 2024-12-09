from aiogram import Bot, Dispatcher
from decouple import config

Admins = [6363784985, ]
token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)