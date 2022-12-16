import sqlite3 as sq
from variables import *


async def db_connect():
    global db, cur

    db = sq.connect(name_db)
    cur = db.cursor()

    cur.execute(create_db)
    db.commit()


async def get_all_users():

    result = cur.execute(select_all).fetchall()

    return result


async def create_new_user(state):

    async with state.proxy() as data:
        result = cur.execute(
            add_user, (data['lastname'], data['name'], data['phone']))
        db.commit()

    return result


async def delete_user(user_id):

    cur.execute(del_user, (user_id,))
    db.commit()


async def edit_user(user_id, state):
    async with state.proxy() as data:
        cur.execute(update_user, (data['lastname'],
                    data['name'], data['phone'], user_id,))
        db.commit()
