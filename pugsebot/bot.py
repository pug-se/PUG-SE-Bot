import gdgajubot.bot

# hack to remove irrelevant easter eggs
for egg_func in 'love_ruby', 'memory_java', 'easter_python':
    delattr(gdgajubot.bot.GDGAjuBot, egg_func)


# our own bot class
class PugSeBot(gdgajubot.bot.GDGAjuBot):
    pass
