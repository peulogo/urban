import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM Users')
conn.commit()

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


cursor.execute('''DELETE FROM Users WHERE id =6''')
conn.commit()


cursor.execute('''SELECT COUNT(*) FROM Users''')
total_users = cursor.fetchall()[0][0]

cursor.execute('''SELECT SUM(balance) FROM Users''')
all_balances = cursor.fetchall()[0][0]

print(all_balances / total_users)
conn.close()

conn.close()
