import discord, random
from discord.ext import commands
from discord import app_commands

bot = commands.Bot("p!", intents=discord.Intents.all(), help_command=None)


async def on_ready():
    print(f"Bot logado em {bot.user.name}")
    comandos = await bot.tree.sync()
    print(f"{len(comandos)} foram sincronizados.")

async def on_message(message: discord.Message):
    if message.author.id == 716390085896962058 and "Please tell us you're human!" in message.content:
        await message.author.kick(reason="captcha nas area")
        await message.channel.send(random.choice(["a patrao eu nao consigo fazer captcha, q nao consegue rapaz segue o orea seca o estilo e esse."]))
    if "desenrolado" in message.content:
        await message.channel.send("tem que ser assim rapaz")
    if "a patrao eu nao consigo" in message.content:
        await message.channel.send("que nao consegue rapaz segue o orea seca aqui o estilo è esse mermao")


@bot.tree.command(name="desenrolado", description="Desenrolado")
async def desenroladocmd(inter: discord.Interaction):
    await inter.response.send_message("Tem q ser assim rapaz")

bot.add_listener(on_message, 'on_message')
bot.add_listener(on_ready, 'on_ready')

bot.run("")