import sqlite3

def initiate_db(db_name='not_telegram.db'):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )
        ''')
    conn.commit()
    conn.close()


def add_user(username, email, age, balance, db_name='not_telegram.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
        ''', (username, email, age, balance))

    conn.commit()
    conn.close()


def is_included(username, db_name='not_telegram.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT 1 FROM Users WHERE username = ?
    ''', (username,))

    result = cursor.fetchone()
    conn.close()
    return result is not None


def get_all_products(db_name='not_telegram.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')

    products = cursor.fetchall()

    conn.close()

    return products
