###########################################################
#
# Ресурс скачан с сайта LEAKED-MINECRAFT.PRO:
# • Лучшего сайта по сливам приватных ресурсов!
# • Прямо сейчас действуют скидки на улучшение аккаунта!
#
# Заходи на наш сайт: https://leaked-minecraft.pro/
#
###########################################################
from discord.ext import commands
from utils import *
from message import *
from discord.ui import Button, View
from random import randint
from module_bd import *
from random import randint
import json

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", help_command=None, intents=intents)

@client.event
async def on_ready():
    print("------------------------------------------------------------")
    print(f"[OP-GOOSEBOT] Токен: {TOKEN}")
    print(f"[OP-GOOSEBOT] Версия: {VERSION}")
    print("")

@client.command(aliases=["рег"])
async def reg(ctx):
    if ctx.message.channel.id == 1037088402727772230:
        author_id = str(ctx.message.author.id)

        random_int = str(randint(111111, 999999))
        random_name = "goose_"+random_int

        with open("bd/bd.json", "r") as bd:
            bd_list = json.load(bd)
        
        if author_id in bd_list.keys():
            await ctx.reply(embed=messages_embed["error_reg"])
        else:
            bd_list[author_id] = {"BALL": 0, "FEED": 3, "EXP": 0, "CLICK": 0, "NAME": random_name}

            with open("bd/bd.json", "w") as bd:
                json.dump(bd_list, bd, indent=4)
            
            await ctx.reply(embed=messages_embed["successfully_reg"])
    else:
        await ctx.reply(embed=messages_embed["error_channel"])

@client.command(aliases=["помощь", "начать"])
async def help(ctx):
    if ctx.message.channel.id == 1037088402727772230:
        author_id = str(ctx.message.author.id)

        with open("bd/bd.json", "r") as bd:
            bd_list = json.load(bd)
        
        async def food_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                ball = bd_list[author_id]["BALL"]
                feed = bd_list[author_id]["FEED"]

                if ball > 9:
                    new_ball = ball - 10
                    new_feed = feed + 1
                    bd_list[author_id]["BALL"] = new_ball
                    bd_list[author_id]["FEED"] = new_feed

                    with open("bd/bd.json", "w") as bd:
                        json.dump(bd_list, bd, indent=4)

                        await interaction.response.send_message(embed=messages_embed["successfully_food"])
                else:
                    await interaction.response.send_message(embed=messages_embed["error_amount_money"])
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)

        async def magazin_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                view = View()
                view.add_item(messages_button["food"])

                messages_button["food"].callback = food_function
                
                await interaction.response.send_message(embed=messages_embed["magazin"], view=view)
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)

        async def clicker_real_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                click = bd_list[author_id]["CLICK"]
                ball = bd_list[author_id]["BALL"]

                new_ball = ball + 1
                new_click = click + 1
                bd_list[author_id]["BALL"] = new_ball
                bd_list[author_id]["CLICK"] = new_click

                with open("bd/bd.json", "w") as bd:
                    json.dump(bd_list, bd, indent=4)

                clicker = discord.Embed(title=messages["title"], description=f"За нажатие по кнопке \"🚀 Клик\", вы будете получать 1 монету.\n\nВы кликнули: {click}", colour=discord.Color.orange())

                await interaction.response.edit_message(embed=clicker)
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)

        async def clicker_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                view = View()
                view.add_item(messages_button["job_clicker"])

                messages_button["job_clicker"].callback = clicker_real_function

                await interaction.response.send_message(embed=messages_embed["job_clicker"], view=view)
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)
        
        async def job_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                view = View()
                view.add_item(messages_button["clicker"])

                messages_button["clicker"].callback = clicker_function

                await interaction.response.send_message(embed=messages_embed["job_menu"], view=view)
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)

        async def feed_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                feed = bd_list[author_id]["FEED"]
                exp = bd_list[author_id]["EXP"]

                if feed > 0:
                    new_feed = feed - 1
                    new_exp = exp + 10
                    bd_list[author_id]["FEED"] = new_feed
                    bd_list[author_id]["EXP"] = new_exp

                    with open("bd/bd.json", "w") as bd:
                        json.dump(bd_list, bd, indent=4)

                        await interaction.response.send_message(embed=messages_embed["successfully_feed"])
                else:
                    await interaction.response.send_message(embed=messages_embed["error_amount_feed"])
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)
        
        async def rename_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                ball = bd_list[author_id]["BALL"]

                if ball > 4999:
                    await interaction.response.send_message(embed=messages_embed["rename"])
                else:
                    await interaction.response.send_message(embed=messages_embed["error_amount_money_rename"])
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)
        
        async def question_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                await interaction.response.send_message(embed=messages_embed["question"])
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)
        
        async def entertainment_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                view = View()
                view.add_item(messages_button["question"])

                messages_button["question"].callback = question_function

                await interaction.response.send_message(embed=messages_embed["entertainment"], view=view)
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)

        async def my_goose_function(interaction):
            if interaction.user.id == ctx.message.author.id:
                view = View()
                view.add_item(messages_button["feed"])
                view.add_item(messages_button["entertainment"])
                view.add_item(messages_button["job"])
                view.add_item(messages_button["magazin"])
                view.add_item(messages_button["rename"])

                messages_button["feed"].callback = feed_function
                messages_button["job"].callback = job_function
                messages_button["rename"].callback = rename_function
                messages_button["magazin"].callback = magazin_function
                messages_button["entertainment"].callback = entertainment_function

                await interaction.response.send_message(embed=profile_goose, view=view)
            else:
                await interaction.response.send_message(embed=messages_embed["error_author"], ephemeral=True)
        
        if author_id in bd_list.keys():
            exp = bd_list[author_id]["EXP"]
            name = bd_list[author_id]["NAME"]
            feed = bd_list[author_id]["FEED"]
            balance = bd_list[author_id]["BALL"]

            profile_goose = discord.Embed(title=messages["title"], description=f"```ВАШ ЛИЧНЫЙ ГУСЬ```\nНик: {name}\nБаланс: {balance}\nОпыт: {exp}\nЕда: {feed}\n\n```все действия проиходят в дс, если вы додик и решили что в реальной жизни, то вы полный додик```", colour=discord.Color.orange())

            view = View()
            view.add_item(messages_button["my_goose"])

            messages_button["my_goose"].callback = my_goose_function

            await ctx.reply(embed=messages_embed["successfully_help"], view=view)
        else:
            await ctx.reply(embed=messages_embed["reg"])
    else:
        await ctx.reply(embed=messages_embed["error_channel"])

@client.command(aliases=["ник"])
async def nick(ctx, *, arg=None):
    if ctx.message.channel.id == 1037088402727772230:
        author_id = str(ctx.message.author.id)
        
        with open("bd/bd.json", "r") as bd:
            bd_list = json.load(bd)
        
        if author_id in bd_list.keys():
            if arg == None:
                await ctx.reply(embed=messages_embed["error_nick"])
            else:
                ball = bd_list[author_id]["BALL"]

                if ball > 2999:
                    bd_list[author_id]["NAME"] = arg
                    new_ball = ball - 3000
                    bd_list[author_id]["BALL"] = new_ball

                    with open("bd/bd.json", "w") as bd:
                        json.dump(bd_list, bd, indent=4)

                        await ctx.reply(embed=messages_embed["successfully_rename"])
                else:
                    await ctx.reply(embed=messages_embed["error_amount_money_rename"])
        else:
            await ctx.reply(embed=messages_embed["reg"])
    else:
        await ctx.reply(embed=messages_embed["error_channel"])

@client.command(aliases=["гусь"])
async def goose(ctx, *, arg=None):
    if ctx.message.channel.id == 1037088402727772230:
        author_id = str(ctx.message.author.id)
        random = randint(1, 3)

        with open("bd/bd.json", "r") as bd:
            bd_list = json.load(bd)
        
        if author_id in bd_list.keys():
            if arg == None:
                await ctx.reply(embed=messages_embed["error_goose"])
            else:
                ball = bd_list[author_id]["BALL"]

                if ball > 4:
                    new_ball = ball - 5
                    bd_list[author_id]["BALL"] = new_ball

                    with open("bd/bd.json", "w") as bd:
                        json.dump(bd_list, bd, indent=4)

                        no_question = discord.Embed(title=messages["title"], description=f"Вопрос: **{arg}**\n\n➥ Ответ: **НЕТ**", colour=discord.Color.red())
                        medium_question = discord.Embed(title=messages["title"], description=f"Вопрос: **{arg}**\n\n➥ Ответ: **ХО-ХО**", colour=discord.Color.orange())
                        yes_question = discord.Embed(title=messages["title"], description=f"Вопрос: **{arg}**\n\n➥ Ответ: **ДА**", colour=discord.Color.green())

                        if random == 1:
                            await ctx.reply(embed=no_question)
                        elif random == 2:
                            await ctx.reply(embed=yes_question)
                        elif random == 3:
                            await ctx.reply(embed=medium_question)
                else:
                    await ctx.reply(embed=messages_embed["error_amount_money_goose"])
        else:
            await ctx.reply(embed=messages_embed["reg"])
    else:
        await ctx.reply(embed=messages_embed["error_channel"])

client.run(TOKEN)