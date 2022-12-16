from aiogram import types, executor, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import TOKEN_API
from keyboards import *
import sqlite_db
import json
from variables import *

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot,
                storage=storage)


class UserStatesGroup(StatesGroup):

    lastname = State()
    name = State()
    phone = State()

    new_lastname = State()
    new_name = State()
    new_phone = State()


async def on_startup(_):
    await sqlite_db.db_connect()
    print('Подключение к БД выполнено успешно')


async def show_all_user(callback: types.CallbackQuery, users):
    for user in users:
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=f'id: {user[0]}\nФамилия: {user[1]}\nИмя: {user[2]}\nТелефон: {user[3]}',
                               reply_markup=get_edit_ikb(user[0]))


async def save_json(data):
    res = {user[0]: dict(zip(headers[1:4], user[1:4])) for user in data}
    with open('book.json', 'w', encoding='utf-8') as fson:
        json.dump(res, fson, ensure_ascii=False, indent=4)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Добро пожаловать!\nКоманда /help расскажет о командах',
                         reply_markup=get_start_kb())


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=help_message,
                           reply_markup=get_start_kb())


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.answer('У нас отмена!', reply_markup=get_start_kb())


@dp.message_handler(commands=['menu'])
async def cmd_users(message: types.Message):
    await message.delete()
    await message.answer('***МЕНЮ***\nВыбери действие!',
                         reply_markup=get_use_ikb())


@dp.callback_query_handler(text='get_all_users')
async def cb_get_all_users(callback: types.CallbackQuery):
    result = await sqlite_db.get_all_users()

    if not result:
        await callback.message.delete()
        await callback.message.answer('Список пуст')
        return await callback.answer()

    await callback.message.delete()
    await show_all_user(callback, result)
    await callback.answer()


@dp.callback_query_handler(text='save')
async def cb_save_users(callback: types.CallbackQuery):
    result = await sqlite_db.get_all_users()

    if not result:
        await callback.message.delete()
        await callback.message.answer('Список пуст')
        return await callback.answer()

    await save_json(result)
    await callback.message.answer('Файл успешно сохранен')
    await callback.answer()


@dp.callback_query_handler(text='add_new_users')
async def cb_add_new_users(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Введите фамилию',
                                  reply_markup=get_cancel_kb())

    await UserStatesGroup.lastname.set()


@dp.message_handler(state=UserStatesGroup.lastname)
async def handle_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text

    await message.reply('Теперь имя')
    await UserStatesGroup.next()


@dp.message_handler(state=UserStatesGroup.name)
async def handle_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('и телефон')
    await UserStatesGroup.next()


@dp.message_handler(state=UserStatesGroup.phone)
async def handle_phone(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply('Это не номер...\nПопробуй еще раз')
    else:
        async with state.proxy() as data:
            data['phone'] = message.text

        await sqlite_db.create_new_user(state)

        await message.reply('Контакт сохранен', reply_markup=get_start_kb())
        await state.finish()


@dp.callback_query_handler(users_cb.filter(action='delete'))
async def cb_delete_user(callback: types.CallbackQuery, callback_data):
    await sqlite_db.delete_user(callback_data['id'])

    await callback.message.reply('Успешно удалён')
    await callback.answer()


@dp.callback_query_handler(users_cb.filter(action='edit'))
async def cb_edit_user(callback: types.CallbackQuery, callback_data, state: FSMContext):
    await callback.message.answer('Редактируем\nУкажи фамилию', reply_markup=get_cancel_kb())
    await UserStatesGroup.new_lastname.set()

    async with state.proxy() as data:
        data['user_id'] = callback_data['id']

    await callback.answer()


@dp.message_handler(state=UserStatesGroup.new_lastname)
async def handle_newlastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text

    await message.reply('Укажи имя')
    await UserStatesGroup.next()


@dp.message_handler(state=UserStatesGroup.new_name)
async def handle_newname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('И телефон')
    await UserStatesGroup.next()


@dp.message_handler(state=UserStatesGroup.new_phone)
async def handle_newphone(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply('Это не номер')
    else:
        async with state.proxy() as data:
            data['phone'] = message.text

        await sqlite_db.edit_user(data['user_id'], state)
        await message.reply('Заменили', reply_markup=get_start_kb())
        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
