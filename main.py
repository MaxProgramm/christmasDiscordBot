import discord
import time
TOKEN = "ENTER_TOKEN_HERE"
# Your message
ChristmasMessage = "Merry Christmas!:christmas_tree::gift: Wünscht der MC World DC-Server"
WaitTime = 0.5

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    if message.content.startswith("!bot"):
        msg = message.content.split(" ")
        if msg[1] == "ChristmasNuke":
            GuildMembers = message.guild.members
            print(GuildMembers)
            for user in GuildMembers:
                if not user.bot:
                    try:
                        await user.send(ChristmasMessage)
                        time.sleep(WaitTime)
                    except:
                        continue



client.run(TOKEN)
