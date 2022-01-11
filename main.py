import discord
from discord.ext import commands
import json

bot=commands.Bot(command_prefix='#', case_insensitive=True)

with open("./config.json", 'r') as configjsonFile:#Token is taken from json file
    configData=json.load(configjsonFile)
    TOKEN=configData["DISCORD_TOKEN"]

@bot.event
async def on_ready():
    print("I am Ready!")

@bot.command()
async def hi(ctx):
    await ctx.send('Hello!')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *,msg):
    embed=discord.Embed(
        title="title",
        description=msg,
        color= discord.Color.red()
    )
    embed.set_author(name= ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name="field 1", value='field value', inline=True)
    embed.add_field(name="field 2", value='field value2', inline=True)
    embed.add_field(name="field 3", value='field value3',inline=False)
    embed.set_footer(text='this is footer')
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_thumbnail(url= ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

bot.run(TOKEN)