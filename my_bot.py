from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я ваш Telegram-бот. Чем могу помочь?")


# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Доступные команды:\n/start - Начать работу\n/help - Получить помощь"
    )


def main():

    # Вставьте ваш токен ниже
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запуск бота
    application.run_polling()


if __name__ == "__main__":
    main()
