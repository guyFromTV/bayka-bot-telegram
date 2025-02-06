from telebot.types import BotCommand

default_commands = [
    BotCommand("start", "start bot"),
    BotCommand('help', "send help message"),
    BotCommand("joke", "random joke"),
    BotCommand("joke2", "random 2 part joke"),
    BotCommand("rub_to_azn", "convert RUB to AZN"),
    BotCommand("cvt", "convert"),
    BotCommand("set_my_currency", "set default currency"),
    BotCommand('quiz', "play a quiz"),
]