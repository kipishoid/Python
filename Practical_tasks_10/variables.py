name_db = 'book_sqlite.db'

headers = ['id', 'Фамилия', 'Имя', 'Телефон']

create_db = '''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            lastname TEXT NOT NULL,
                            name TEXT NOT NULL,
                            phone TEXT NOT NULL);'''


select_all = '''SELECT * FROM users'''

add_user = '''INSERT INTO users (lastname, name, phone) VALUES (?, ?, ?);'''

del_user = """DELETE FROM users WHERE user_id = ?"""

update_user = """UPDATE users SET lastname = ?, name = ?, phone = ? WHERE user_id = ?"""


help_message = "Это телефоная книга\n" \
               "Доступные команды:\n" \
               "/start - Приветствие и вызов кнопки menu\n" \
               "/menu - Вызов меню " \
               "инлайн клавиатуры: \n" \
               "Просмотр всех\n" \
               "Добавить новый\n" \
               "Сохранить в файл\n"
