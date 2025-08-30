# bot.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8322788899:AAFbhvNYkXl__NGaXEGkt2ZjtVle4G4ADYM"
WEBAPP_URL = "https://tgbot-mu-seven.vercel.app/"  # ngrok yoki Vercel manzilingiz

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[ InlineKeyboardButton("Open Mini App", web_app=WebAppInfo(url=WEBAPP_URL)) ]]
    await update.message.reply_text("Mini-appni ochish uchun tugmani bosing:", reply_markup=InlineKeyboardMarkup(kb))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
