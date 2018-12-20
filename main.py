import discord
import asyncio
import subprocess
import re
import random

client = discord.Client()

x = ["死んで", "悪徳", "勝ち", "死ね", "うんこ", "かと。", "ない。", "クソ", "糞", "ガイジ", "ホラホラ", "ぜ。", "...", "！ｗ"]
def compel_message_akutoku(user_message):
    for i in x:
        if i in user_message:
            return True
    return False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if re.match("こんにちは", message.content):
        if client.user != message.author:
            m = message.author.mentionm + "こんにちは"

    if compel_message_akutoku(message.content):
        if client.user != message.author:
            rand = random.randint(1, 10)
            if rand < 3:
                m = "一興かと。"
            elif rand < 9:
                m = message.author.mention + "はい悪徳"
            else:
                m = message.author.mention + "m9 はい終命の屑～"
            await client.send_message(message.channel, m)

    if message.content.startswith("トイレに行ってもいいですか？"):
        if client.user != message.author:
            m = "駄目です。"
            await client.send_message(message.channel, m)
    

client.run("DISCORD_BOT_TOKEN")