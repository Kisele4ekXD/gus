###########################################################
#
# Ресурс скачан с сайта LEAKED-MINECRAFT.PRO:
# • Лучшего сайта по сливам приватных ресурсов!
# • Прямо сейчас действуют скидки на улучшение аккаунта!
#
# Заходи на наш сайт: https://leaked-minecraft.pro/
#
###########################################################
import discord
from discord.ui import Button

messages = {
    "title": "Leaked-Minecraft.pro💫",
    "reg": "У вас нет гуся, создайте гуся!\n\n➥ создать гуся: **!рег**",
    "error_channel": ":no_entry_sign: Я работаю в канале: **🦆・говорящий-гусь**",
    "error_reg": "У вас уже есть гусь.\n\n➥ что-бы управлять напишите **!помощь**",
    "successfully_reg": "Вы успешно создали гуся, теперь вы можете:\n\n• Кормить,\n• Поить,\n• Играть,\n• Работать.\n\n➥ что-бы управлять напишите **!помощь**",
    "successfully_help": "У вас есть гусь, вы можете:\n\n• Кормить,\n• Поить,\n• Играть,\n• Работать.\n\n➥ что-бы управлять нажмите \"🦆 Мой гусь\"",
    "error_author": "Данное взаимодействие доступно только отправителю комманды, если это необходимо напишите комманду связанную с данным взаимодействием.",
    "error_amount_feed": "У вас недостаточно еды, что-бы покормить гуся!\n\n➥ просмотр еды: **!помощь**",
    "successfully_feed": "Вы успешно покормили гуся, и получили **+10 ОПЫТА**",
    "magazin": "Выберите товар:\n\nЕда | 1шт. = 10 монет.",
    "error_amount_money": "У вас недостаточно монет, что-бы купить товар!\n\n➥ просмотр баланса: **!помощь**",
    "successfully_food": "Вы успешно купили товар: **Еда | 1шт.**",
    "job_menu": "Выберите работу:",
    "job_clicker": "За нажатие по кнопке \"🚀 Клик\", вы будете получать 1 монету.",
    "rename": "Что-бы сменить имя гуся, напишите: **!ник**",
    "error_amount_money_rename": "У вас недостаточно монет, что-бы купить смену ника!\nСмена ника стоит: **3.000 монет**\n\n➥ просмотр баланса: **!помощь**",
    "error_nick": "Вы не ввели имя гусю, введите имя гусю, как показана в примере\n\n➥ пример: **!ник [новый_ник]**",
    "successfully_rename": "Вы успешно сменили имя гуся!",
    "error_goose": "Вы не ввели вопрос, введите вопрос гусю, как показана в примере\n\n➥ пример: **!гусь [вопрос]**",
    "error_amount_money_goose": "У вас недостаточно монет, что-бы задать вопрос!\nВопрос стоит: **5 монет**\n\n➥ просмотр баланса: **!помощь**",
    "entertainment": "Выберите развлечение:",
    "question": "Что-бы поиграть в \"❔Вопрос - ответ\", напишите сообщение которое показана в примере.\n\n➥ пример: **!гусь [вопрос]**"
}

messages_embed = {
    "reg": discord.Embed(title=messages["title"], description=messages["reg"], colour=discord.Color.red()),
    "error_reg": discord.Embed(title=messages["title"], description=messages["error_reg"], colour=discord.Color.orange()),
    "error_channel": discord.Embed(title=messages["title"], description=messages["error_channel"], colour=discord.Color.red()),
    "successfully_reg": discord.Embed(title=messages["title"], description=messages["successfully_reg"], colour=discord.Color.green()),
    "successfully_help": discord.Embed(title=messages["title"], description=messages["successfully_help"], colour=discord.Color.orange()),
    "error_author": discord.Embed(title=messages["title"], description=messages["error_author"], colour=discord.Color.red()),
    "error_amount_feed": discord.Embed(title=messages["title"], description=messages["error_amount_feed"], colour=discord.Color.red()),
    "successfully_feed" : discord.Embed(title=messages["title"], description=messages["successfully_feed"], colour=discord.Color.green()),
    "magazin": discord.Embed(title=messages["title"], description=messages["magazin"], colour=discord.Color.orange()),
    "error_amount_money": discord.Embed(title=messages["title"], description=messages["error_amount_money"], colour=discord.Color.red()),
    "successfully_food": discord.Embed(title=messages["title"], description=messages["successfully_food"], colour=discord.Color.green()),
    "job_menu": discord.Embed(title=messages["title"], description=messages["job_menu"], colour=discord.Color.orange()),
    "job_clicker": discord.Embed(title=messages["title"], description=messages["job_clicker"], colour=discord.Color.orange()),
    "rename": discord.Embed(title=messages["title"], description=messages["rename"], colour=discord.Color.orange()),
    "error_amount_money_rename": discord.Embed(title=messages["title"], description=messages["error_amount_money_rename"], colour=discord.Color.red()),
    "error_nick": discord.Embed(title=messages["title"], description=messages["error_nick"], colour=discord.Color.red()),
    "successfully_rename": discord.Embed(title=messages["title"], description=messages["successfully_rename"], colour=discord.Color.green()),
    "error_goose": discord.Embed(title=messages["title"], description=messages["error_goose"], colour=discord.Color.red()),
    "error_amount_money_goose": discord.Embed(title=messages["title"], description=messages["error_amount_money_goose"], colour=discord.Color.red()),
    "entertainment": discord.Embed(title=messages["title"], description=messages["entertainment"], colour=discord.Color.orange()),
    "question": discord.Embed(title=messages["title"], description=messages["question"], colour=discord.Color.orange())
}

messages_button = {
    "my_goose": Button(label="Мой гусь", style=discord.ButtonStyle.green, emoji="🦆"),
    "rename": Button(label="Смена ника", style=discord.ButtonStyle.green, emoji="📄"),  
    "feed": Button(label="Покормить", style=discord.ButtonStyle.green, emoji="🍗"),
    "job": Button(label="Работа", style=discord.ButtonStyle.green, emoji="🪙"),
    "magazin": Button(label="Магазин", style=discord.ButtonStyle.green, emoji="🛒"),
    "food": Button(label="Еда | 1шт.", style=discord.ButtonStyle.green, emoji="🍔"),
    "clicker": Button(label="Кликер", style=discord.ButtonStyle.green, emoji="🖱️"),
    "job_clicker": Button(label="Клик", style=discord.ButtonStyle.green, emoji="🚀"),
    "entertainment": Button(label="Развлечения", style=discord.ButtonStyle.green, emoji="🎉"),
    "question": Button(label="Вопрос - ответ", style=discord.ButtonStyle.green, emoji="❔")
}