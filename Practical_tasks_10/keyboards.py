from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

users_cb = CallbackData('users', 'id', 'action')


def get_use_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Просмотр всех', callback_data='get_all_users')],
        [InlineKeyboardButton(
            'Добавить новый', callback_data='add_new_users')],
        [InlineKeyboardButton('Сохранить в json', callback_data='save')]
    ])

    return ikb


def get_edit_ikb(user_id):
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            'Редактировать', callback_data=users_cb.new(user_id, 'edit'))],
        [InlineKeyboardButton(
            'Удалить', callback_data=users_cb.new(user_id, 'delete'))]
    ])
    return ikb


def get_start_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('/menu')]
    ], resize_keyboard=True)

    return kb


def get_cancel_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('/cancel')]
    ], resize_keyboard=True)
    return kb
