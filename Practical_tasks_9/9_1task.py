from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message

TOKEN = ''

logging.basicConfig(level=logging.INFO)

API_TOKEN = TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

value = ''
old_value = ''

keyboard = InlineKeyboardMarkup()
keyboard.row(types.InlineKeyboardButton("(", callback_data="("),
             types.InlineKeyboardButton(")", callback_data=")"),
             types.InlineKeyboardButton("<=", callback_data="<="),
             types.InlineKeyboardButton("/", callback_data="/"))

keyboard.row(types.InlineKeyboardButton("7", callback_data="7"),
             types.InlineKeyboardButton("8", callback_data="8"),
             types.InlineKeyboardButton("9", callback_data="9"),
             types.InlineKeyboardButton("*", callback_data="*"))

keyboard.row(types.InlineKeyboardButton("4", callback_data="4"),
             types.InlineKeyboardButton("5", callback_data="5"),
             types.InlineKeyboardButton("6", callback_data="6"),
             types.InlineKeyboardButton("-", callback_data="-"))

keyboard.row(types.InlineKeyboardButton("1", callback_data="1"),
             types.InlineKeyboardButton("2", callback_data="2"),
             types.InlineKeyboardButton("3", callback_data="3"),
             types.InlineKeyboardButton("+", callback_data="+"))

keyboard.row(types.InlineKeyboardButton("C", callback_data="C"),
             types.InlineKeyboardButton("0", callback_data="0"),
             types.InlineKeyboardButton(",", callback_data="."),
             types.InlineKeyboardButton("=", callback_data="="))


@dp.message_handler(commands='calc')
async def get_message(message: types.Message):
    global value
    if value == '':
        await bot.send_message(message.from_user.id, 'Калькулятор', reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@dp.callback_query_handler(lambda call: True)
async def callback_function(query: types.CallbackQuery):
    global value, old_value
    data = query.data

    if data == "no":
        pass
    elif data == "C":
        value = ""
    elif data == "<=":
        if value != '':
            value = value[:len(value)-1]
    elif data == "=":
        try:
            value = str(eval(value))
        except:
            value = "Ошибка!"
    else:
        value += data

    if value != old_value:
        if value == '':
            await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)

        old_value = value


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхо-бот!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
