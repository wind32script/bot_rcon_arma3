import discord
import datetime
import asyncio
import berconpy
import random
msgcount11 = 0
import asyncio
import berconpy

client = berconpy.AsyncRCONClient()
IP = '127.0.0.1'
PORT = 2310
PASSWORD = "rcon123123cfcjhasdf"

@client.dispatch.on_login
async def on_login():
    print('Подключение к RCON')

 

async def main():
    async with client.connect(IP, PORT, PASSWORD):
        players= await client.send_command("#monitor")
        print('Включение монитора')
       
        while True:
            global msgcount11
            msgcount11 = msgcount11 + 1
            if msgcount11 > 5:
                msg = arma_msg()
                await client.send_command("Say -1 "+ msg)
                print(msg)
                msgcount11 = 0
            now = datetime.datetime.now()
            # Получаем текущие часы и минуты.
            hours = now.hour
            minutes = now.minute

            # Проверяем условие
            if hours % 4 == 3 and minutes == 45:
                msg = 'ВНИМАНИЕ До рестарта 15 минут!'
                await client.send_command("Say -1 "+ msg)
                print(msg)
                
            # Проверяем условие
            if hours % 4 == 3 and minutes == 30:
                msg = 'ВНИМАНИЕ До рестарта 30 минут!'
                await client.send_command("Say -1 "+ msg)
                print(msg)
                
             # Проверяем условие
            if hours % 4 == 3 and minutes == 55:
                msg = 'ВНИМАНИЕ До рестарта 5 минут!'
                await client.send_command("Say -1 "+ msg)
                print(msg)
                
             # Проверяем условие
            if hours % 4 == 3 and minutes == 58:
                msg = 'ВНИМАНИЕ До рестарта 1 минута!'
                await client.send_command("Say -1 "+ msg)
                print(msg)
                
            await asyncio.sleep(55)  # пауза в 60 секунд
 

def arma_msg():
    with open('bot_msg.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
            # Удаляем символ новой строки из каждой строки
        lines = [line.strip() for line in lines]
        random_line = random.choice(lines)
        return random_line


asyncio.run(main())
