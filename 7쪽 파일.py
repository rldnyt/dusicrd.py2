@client.event 
async def on_member_join(member): # 방에 멤버가 들어왔을때
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    now = datetime.datetime.now()
    embed = discord.Embed(color=0x00ff00)
    embed.add_field(name="닉네임", value=member.name, inline=True)
    embed.add_field(name="디스코드 가입일", value=str(date.year) + "년도" + str(date.month) + "월" + str(date.day) + "일",inline=True)
    embed.add_field(name="우소공 가입일",value=str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second), inline=False)
    embed.set_thumbnail(url=member.avatar_url)

    channel = client.get_channel(id=678190016156925984) # id= 후에 채널 아이디을 넣으면 거기로 가짐
    await channel.send(embed=embed) # 임베트 출력
