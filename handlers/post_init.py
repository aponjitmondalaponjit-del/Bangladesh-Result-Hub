from telegram import BotCommand


async def post_init(application):
    await application.bot.set_my_commands([
        BotCommand("settings", "⚙️ Settings"),
        BotCommand("support", "🆘 Support"),
        BotCommand("premium", "💎 Premium"),
    ])
