import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("정상작동중")
    game = discord.Game("치킨아이리와 /help")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("치킨아이리와"):
        await message.channel.send("따끈따끈한 치킨봇 나왔습니다! 어떤것을 도와드릴까요?")
    if message.content.startswith("/도와줘:서버"):
        await message.channel.send("서버를 만드실건가요? 만드실거면 /도와줘;서버 Y 만들지 않으실거면 /도와줘;서버 N을 해주세요")
    if message.content.startswith("/도와줘;서버 Y"):
        await message.channel.send("서버 만드는 방법은 플러스버튼을 누르고 서버 생성하기를 누르시면 됩니다! 그리고 서버위치 서버이름을 설정할수있어요! 설정뒤에는 생성을 누르시면 생성이됩니다! 초대코드로 친구들을 초대해보세요!")
    if message.content.startswith("/도와줘;서버 N"):
        await message.channel.send("어떤것을 도와드릴까요?")
    if message.content.startswith("/help"):
        await message.channel.send("[/도와줘:서버] , [/도와줘:통화] 등등 디스코드를 처음 입문하신분들께 굉장히 유리한 치킨봇입니다!")
    if message.content.startswith("/도와줘:통화"):
        await message.channel.send("친구분이랑 하시나요? 친구Y 친구N 중에 해주세요")
    if message.content.startswith("/친구Y"):
        await message.channel.send("친구분의 닉네임과 디스코드 태그를 친구추가목록에 해주세요! 예시 discord#1234 이렇게 해주신후 친구요청을 보내면 친구가 그 요청을 받고 전화를 걸수있게 됩니다! 전화거는 방법은 맨위에 있는 수화기 모양의 버튼을 누르시면 전화가 갑니다!")
    if message.content.startswith("/친구N"):
        await message.channel.send("친구분끼리 하지 않으신다면.. 그건 제가 해결해드리긴 어렵겠네요 ㅠㅠ 죄송합니다 ㅠㅠ 하지만! 더 열심히 노력하는 치킨이봇이 될게요! (づ￣ 3￣)づ")






client.run("NjM5NzA5Njc5OTI0MjgxMzQ1.XbvOdw.ER2GfV7b7Qmb1pcXpZgbSwsAdqg")