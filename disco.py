import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("안녕봇 & ;;help")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith(";;안녕하세요"):
        await message.channel.send("네 안녕하세요 저희 서버에 와주셔서 정말로 감사합니다!")
    if message.content.startswith("안녕봇"):
        await message.channel.send("안녕하세요! 전 안녕봇이라고 해요! 다른 명령어가 궁금하시면 ;;을 쳐주세요!")
    if message.content.startswith(";;help"):
        await message.channel.send("저와 놀고싶으시다면 ;;놀자 를 쳐주시고 공지사항을 보고싶으시다면 ;;공지사항을 쳐주세요! 아직 미완성이라 모자랄수도 있어요!")
    if message.content.startswith(";;놀자"):
        await message.channel.send("죄송합니다 ㅠㅠ 아직 놀자기능은 열리지 않았어요 ㅠㅠ 더더욱 꾸준한 패치로 여러분들을 반기겠습니다!")
    if message.content.startswith(";;공지사항"):
        await message.channel.send("오늘의 공지사항은 없다네요! 봐주셔서 감사합니다!")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
