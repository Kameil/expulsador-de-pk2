import discord
from discord.ext import commands

bot = commands.Bot("p!", intents=discord.Intents.all(), help_command=None)


async def on_message(message: discord.Message):
    if message.author.id == 716390085896962058 and "Please tell us you're human!" in message.content:
        await message.author.kick(reason="captcha nas area")
        await message.channel.send("atividade para nao virar saudade")


bot.add_listener(on_message, 'on_message')

bot.run("")
