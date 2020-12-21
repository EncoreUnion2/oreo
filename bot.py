import discord
from discord.ext import commands
from discord.utils import get

TOKEN = 'NzYyMjY5MzY1ODE4MDk3Njc0.X3msqw.rrZ9vaYlo1p2n3qCRDTC2XQ3e8U'

bot = commands.Bot(command_prefix='>', intents = discord.Intents.all())
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print('Бот запущен.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Шрэк Навсегда"))



# @bot.event
# async def on_member_join(member):
# 	guild = member.guild
# 	channel = get(guild.channels, id = "777580263412596767")
# 	await channel.edit(name = f'Учатники: {guild.member_count}')


# @bot.event
# async def on_member_remove(member):
# 	guild = member.guild
# 	channel = get(guild.channels, id = "777580263412596767")
# 	await channel.edit(name = f'Учатники: {guild.member_count}')


@bot.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Подписчик☄️")
    await ctx.add_roles(role)

bot.run(TOKEN)
