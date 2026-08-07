from telegram import BotCommand, MenuButtonCommands
from telegram.ext import Application


async def post_init(app: Application):

    await app.bot.set_my_commands([
        BotCommand("start", "🏠 Main Menu"),
        BotCommand("settings", "⚙️ Settings"),
        BotCommand("support", "🆘 Support"),
        BotCommand("premium", "💎 Premium"),
    ])

    await app.bot.set_chat_menu_button(
        menu_button=MenuButtonCommands()
    )
