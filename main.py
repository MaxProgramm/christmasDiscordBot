import discord
import time
TOKEN = "ENTER_TOKEN_HERE"

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
                        await user.send("Merry Christmas!:christmas_tree::gift: Wünscht der MC World DC-Server")
                        time.sleep(0.5)
                    except:
                        continue

    if "https://" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Don't send links!")
    else:
        return



client.run(TOKEN)
