from mcrcon import MCRcon
import discord
from discord.ext import commands

def runCommand(cmd: str):
    with MCRcon("localhost", "sekret",25566) as mcr:
        try:
            resp = mcr.command(cmd)
        except Exception as e:
            return e
    return resp


token = ""

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.tree.command(name="run", description="Summoning a adolf hitler in real life")
async def commandRun(interaction: discord.Interaction, cmd: str):
    result = runCommand(cmd)
    print(result)
    await interaction.response.send_message(embed=discord.Embed(title="RCON RESULT",description=f"Result command:\n```{result}```"))

bot.run(token)