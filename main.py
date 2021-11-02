from keep_alive import keep_alive
import os
import discord, json
from discord.ext import commands
import discord
from discord import member
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)
bot.remove_command("help")

inter_client = InteractionClient(bot)

@bot.event
async def on_ready():
    print(f'Вы вошли как {bot.user}')

@bot.command()
async def verif(ctx):

    emb = discord.Embed(
        description = 
        f"""
        Здраствуйте вы попали на сервер {ctx.guild.name}, пройдите верификацию чтобы получить доступ к другим каналам.
        """,
        colour = 0xFF8C00
    )
    emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/772850448892690462/880752123418136596/947d1f802c858b540b84bc3000fc2439_1_-removebg-preview.png')
    emb.set_author(name = 'Верификация')

    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Верифицироваться',
            custom_id = 'verif_button'
        )
    )
    await ctx.send(embed = emb, components = [row])

@bot.event
async def on_button_click(inter):

    res = 'Вы успешно верифицировались!' # ваш вывод сообщение что человек получил роль
    guild = bot.get_guild(inter.guild.id)

    if inter.component.id == "verif_button":
        verif = guild.get_role(***)
        member = inter.author
        await member.add_roles(verif)
        await inter.reply(res, ephemeral = True)
 
keep_alive()
bot.run("***")
