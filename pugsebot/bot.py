import logging
import random

import gdgajubot.bot
from gdgajubot.decorators import *

from pugsebot.resources import zen4java

# hack to remove irrelevant easter eggs
for egg_func in 'love_ruby', 'memory_java', 'easter_python':
    delattr(gdgajubot.bot.GDGAjuBot, egg_func)


# our own bot class
class PugSeBot(gdgajubot.bot.GDGAjuBot):
    @command('/about')
    def about(self, message):
        logging.info("%s: %s", message.from_user.name, "/about")
        response = "Este é o bot do Python User Group de Sergipe (PUG-SE). "
        response += "Para saber mais ou contribuir: https://github.com/pug-se/PUG-SE-Bot"
        self.bot.send_message(message.chat.id, response)

    @easter_egg(r"(?i)\bJAVA\b")
    def zen_for_java(self, message):
        logging.info("%s: %s", message.from_user.name, "zen for java")
        message.reply_text(random.choice(zen4java), quote=False)
