import discord
import os
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.utils import find, get

# Following code loads the .env file located
# Can be commented out if the user wishes to use there own token
# just be sure to assign TOKEN your token value
from dotenv import load_dotenv
from dotenv.main import find_dotenv
load_dotenv(find_dotenv())
TOKEN = os.environ.get("DISCORD_TOKEN")

COUNT = 0
# This line sets the prefix for any user activatable commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents = intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def retrieve(ctx):
    guild = ctx.guild
    # Finds the required roles needed in the guild
    inperson = get(guild.roles, name = "In-Person")
    online = get(guild.roles, name = "Online")

    teams = list()
    teams = get(guild.roles, colour=discord.Colour(0x95a5a6))
    listOfTeams = iter(teams)

    for currentTeam in listOfTeams:
        for member in currentTeam.members:
            if member.has_role(inperson):
                await ctx.send(f'Hey {currentTeam}, Please head to the judging room')
            elif member.has_role(online):
                channel = discord.utils.get(guild.voice_channels, name = "Judging Room")
                await member.move_to(channel)
            else:
                pass
        upcomingTeam = next(listOfTeams)
        await ctx.send(f'Hey {upcomingTeam}, Your team is up next for judging, so get ready. If you are online, please head to the Judging waiting room voice channel. If you are in person, head to the front desk.')

bot.run(TOKEN)