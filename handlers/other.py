from aiogram import types, Dispatcher
from config import bot, dp

async def echo_send(message: types.Message):
    """бот принимает в себя не распознанное сообщение и отпраляет сообщение"""
    await message.reply('Бот не распознал команду /help')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)