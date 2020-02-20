from typing import Dict, Any

import discord
import asyncio

sea={}  # type: Dict[Any, Any]
countG = 0
client = discord.Client()
bot = 'Njc5NjEwNTQ2NjQzMDA5NTM4.Xk3P4w.Y6lHzVaZE1-mldxOpY-04rww86c'

@client.event
async def on_ready():
    print("login")



@client.event
@asyncio.coroutine
async def on_message(message):
    global sea
    if message.content.startswith("/명령어"):
        channel = message.channel
        embed = discord.Embed(
            title = "명령어",
            colour = discord.Colour.red()
        )
        embed.add_field(name="/총내역", value="총 내역을 확인합니다.", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("/총내역"):
        sea = "https://www.youtube.com"  # type: str
        await  message.channel.send("/비밀번호 <비번> 입력하세요")

    if message.content.startswith("/비밀번호"):
        if not sea:
            await  message.channel.send("실패")
        else:
            await message.channel.send("활성화")
