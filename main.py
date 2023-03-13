from settings import settings
import discord
# import * - это тоже самое, что перечислить все файлы
from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)


# Когда бот будет готов, он напишет в консоли свое название!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Когда бот будет получать сообщение, он будет отправлять в этот же канал какие-то сообщения!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Я не понимаю такую команду!")

client.run(settings["TOKEN"])
