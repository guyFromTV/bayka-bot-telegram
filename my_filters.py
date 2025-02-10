from telebot.custom_filters import (
    SimpleCustomFilter,
    AdvancedCustomFilter,
)
from telebot import types
import config

class IsUserAdminOfBot(SimpleCustomFilter):
    key = "is_bot_admin"

    def check(self, message: types.Message):
        return message.from_user.id in config.BOT_ADMIN_USER_ID




class Message_has_entities(SimpleCustomFilter):
    key = "has_entities"

    def check(self, message: types.Message):
        return bool(message.entities)