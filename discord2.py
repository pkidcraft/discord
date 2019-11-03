import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print("정상작동중")
    game = discord.Game("치츠봇이리와 & $help")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("하이"):
        await message.channel.send("네 안녕하세요 저희 서버에 와주셔서 정말로 감사합니다!")
    if message.content.startswith("치즈봇이리와"):
        await message.channel.send("안녕하세요! 전 치즈봇이라고 해요! 여러분들이 좋아하시는 모짜렐라 인더버거에 들어갔던 그 모짜렐라 치즈입니다! 반갑습니다!")
    if message.content.startswith("$help"):
        await message.channel.send("$놀자치츠야 , $공지사항")
    if message.content.startswith("$놀자치즈야"):
        await message.channel.send("죄송합니다 ㅠㅠ 아직 놀자치즈야기능은 열리지 않았어요 ㅠㅠ 더더욱 꾸준한 패치로 여러분들을 반기겠습니다!")
    if message.content.startswith("$공지사항"):
        await message.channel.send("오늘의 공지사항은 없다네요! 봐주셔서 감사합니다!")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)



