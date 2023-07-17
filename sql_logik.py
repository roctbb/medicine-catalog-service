# coding: utf8
import sqlite3
from os import remove


def create_database(data, path):
    try:
        remove(path)
    except:
        pass
    # Connect to SQLite database
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # Создание таблицы "hil"
    table_columns = set()
    for item in data:
        table_columns.update(item.keys())

    cursor.execute('DROP TABLE IF EXISTS hil')
    cursor.execute(f'CREATE TABLE hil (id INTEGER PRIMARY KEY, {", ".join(table_columns)})')

    # Вставка данных
    for item in data:
        placeholders = ', '.join('?' * len(item))
        query = f'INSERT INTO hil ({", ".join(item.keys())}) VALUES ({placeholders})'
        cursor.execute(query, tuple(item.values()))

    conn.commit()
    conn.close()


def get_by_query(letters: str) -> list:
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        query = "SELECT * FROM hil WHERE name_l LIKE ?"
        return cursor.execute(query, ('%' + letters.lower() + '%',)).fetchall()


def get_all_by_id(id: int):
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Запрос на получение данных по указанному ID
    query = "SELECT * FROM hil WHERE id = ?"
    cursor.execute(query, (id,))
    data = cursor.fetchone()

    # Получаем имена столбцов
    column_names = [description[0] for description in cursor.description]

    # Закрываем соединение с базой данных
    conn.close()

    # Создаем словарь с данными
    result = dict(zip(column_names, data))

    return result


def get_name_by_id(id: int) -> str:
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Запрос на получение данных по указанному ID
    query = "SELECT name FROM hil WHERE id = ?"
    cursor.execute(query, (id,))
    data = cursor.fetchone()

    # Закрываем соединение с базой данных
    conn.close()

    # Создаем словарь с данными
    result = data[0]

    return result
