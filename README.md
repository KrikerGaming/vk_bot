<h1 align="center">
  VK BOT на VkBottle
</h1>
<p align="center">
    <em><b>Простой бот для своего проекта</b></em>
</p>

## Hello World

```python
from vkbottle.bot import Bot

bot = Bot("GroupToken")

@bot.on.message()
async def handler(_) -> str:
    return "Hello world!"
    
bot.run_forever()
```

## Документация по vkbottle, если нужно

[Туториал для новичков](https://vkbottle.readthedocs.io/ru/latest/tutorial/)\
[Техническая документация](https://vkbottle.readthedocs.io/ru/latest)

## Установка

Установить новейшую версию можно командой:

```shell
pip install vkbottle
```
