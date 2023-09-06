import discord
import random
pcgames = ["God of War(2018)", "Minecraft", "Geometry Dash", "People Playground", "Idle Research"]
mobgames = ["Eatventure", "Minecraft", "Idle Research", "Zombie Catcher"]
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

#client = discord. Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return
    if message.content.startswith('hellobruv') or message.content.startswith('-greet'):
        await message.channel.send("Hi!")
    elif message.content.startswith('-bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('-pcgameidea'):
        pcgame = random.choice(pcgames)
        await message.channel.send(pcgame, "is a good game, you should try it!")
    elif message.content.startswith('-mobilegameidea'):
        mobgame = random.choice(mobgames)
        await message.channel.send(mobgame, "is a good game, you should try it!")


    elif message.content.strip():  # Check if message content is non-empty
        await message.channel.send(message.content)
    else:
        #await message.channel.send(message.content)
        await message.channel.send("else düştün")
        await message.channel.send(message.content + "dedin")


client.run("MTEyODM2Mzg2ODg2ODA1OTE5Ng.GY6oOp.Bqyzo3BN3C64pTeiFNLCTTCCxETOKQdcjEqVXo")