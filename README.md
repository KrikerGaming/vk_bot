<h1 align="center">
  VK BOT на VkBottle с регистрацией
</h1>
<p align="center">
    <em><b>Простой бот с регистрацией для своего проекта</b></em>
</p>

* [Установка](#Установка)
* [Bot с регистрацией](#Bot-с-регистрацией)
	- [В случае если не работает (или не создается файл) то вот скрипт](##В-случае-если-не-работает-(или-не-создается-файл)-то-вот-скрипт)
* [Документация по vkbottle, если нужно](#Документация-по-vkbottle,-если-нужно)
# Установка

Установить новейшую версию можно командой:

```shell
pip install vkbottle
```

# Bot с регистрацией

```python
import sqlite3
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text, KeyboardButtonColor
import datetime
from datetime import datetime

vk_bot = Bot("GroupToken")

# создаем базу данных и таблицу users, если их нет
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, tag TEXT, balance INTEGER, regDate TEXT)''')
conn.commit()

# команда /reg для регистрации пользователя
@vk_bot.on.message(text="/reg")
async def register_user(message: Message):
    user_id = message.from_id
    tag = message.from_id  # здесь можно заменить на имя пользователя, если оно известно
    reg_date = message.date

    cursor.execute(f"INSERT INTO users (id, tag, balance, regDate) VALUES ({user_id}, '{tag}', 1000, '{reg_date}')")
    conn.commit()

    await message.answer("Вы успешно зарегистрировались!")

# команда /balance для получения баланса пользователя
@vk_bot.on.message(text="/balance")
async def get_balance(message: Message):
    user_id = message.from_id
    cursor.execute(f"SELECT balance FROM users WHERE id={user_id}")
    balance = cursor.fetchone()[0]
    await message.answer(f"Ваш баланс: {balance}")


# команда /profile для получения статистики пользователя
@vk_bot.on.message(text="/profile")
async def get_profile(message: Message):
    user_id = message.from_id

    cursor.execute(f"SELECT tag, balance, regDate FROM users WHERE id = {user_id}")
    result = cursor.fetchone()
    tag, balance, reg_date = result
    reg_date = int(reg_date)

    await message.answer(f"Имя пользователя: {tag}\nБаланс: {balance} руб.\nДата регистрации: {datetime.fromtimestamp(reg_date).strftime('%Y-%m-%d %H:%M:%S')}")

# Запуск бота
vk_bot.run_forever()
```

## В случае если не работает (или не создается файл) то вот скрипт

```python
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

```
# Документация по vkbottle, если нужно

[Туториал для новичков](https://vkbottle.readthedocs.io/ru/latest/tutorial/)\
[Техническая документация](https://vkbottle.readthedocs.io/ru/latest)

