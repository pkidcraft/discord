import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print("이동성공 정상 작동중")
    game = discord.Game("그랜아이리와 !help")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("반갑습니다 ^^ 저희 서버에 오셔서 저 그랜봇은 정말로 감사하게 생각하고 있어요!")
    if message.content.startswith("그랜아이리와"):
        await message.channel.send("KTX의 속도로 달려왔습니다 무엇이 필요하신가요?")
    if message.content.startswith("!help"):
        await message.channel.send("현재 봇이 이동되어서 약간 명령어가 없습니다 ㅠㅠ 수월한 패치로 여러분들을 반기겠습니다!")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
