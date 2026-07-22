def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bangladesh Result Hub (BRH) Started...")

    app.run_polling()
