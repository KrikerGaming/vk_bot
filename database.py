import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create Users table
cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        tag TEXT,
        balance INTEGER,
        ban INTEGER
    )
''')

# Add default user
cursor.execute('INSERT INTO Users (id, tag, balance, ban) VALUES (?, ?, ?, ?)',
               (0, 'default', 1000, 0))
cursor.execute("ALTER TABLE users ADD COLUMN regDate TEXT")

conn.commit()
conn.close()
