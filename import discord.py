import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    game = discord.Game("배틀그라운드")



@client.event
async def on_message(message):
    if message.content.startswith("배틀그라운드"):
        await message.channel.send("배틀그라운드갓겜!")



client.run("")