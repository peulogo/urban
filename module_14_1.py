import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')


users_data = [
    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
    for i in range(1, 11)
]

cursor.executemany('''
INSERT INTO Users (username, email, age, balance) 
VALUES (?, ?, ?, ?)
''', users_data)
conn.commit()

cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
''')
conn.commit()

cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 1
''')
conn.commit()


cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')


records = cursor.fetchall()
for record in records:
    print(f"Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}")

conn.close()
