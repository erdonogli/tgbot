import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8322788899:AAFbhvNYkXl__NGaXEGkt2ZjtVle4G4ADYM"  # BotFather dan olingan tokenni shu yerga yozing

# Coin narxini olish funksiyasi
def get_price(coin="bitcoin", currency="usd"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
        response = requests.get(url).json()
        return response[coin][currency]
    except:
        return None

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom! Men kripto narxlarini ko‘rsatadigan botman.\n\n"
        "ℹ️ Foydalanish:\n"
        "👉 /price btc\n"
        "👉 /price eth\n"
        "👉 /price doge\n"
        "Istalgan coin qisqartmasini yozishingiz mumkin!"
    )

# /price komandasi
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("❌ Iltimos, coin nomini yozing. Masalan: /price btc")
        return

    coin_name = context.args[0].lower()

    # CoinGecko’da coin nomlari to‘liq bo‘lishi kerak: btc -> bitcoin, eth -> ethereum
    mapping = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "doge": "dogecoin",
        "bnb": "binancecoin",
        "sol": "solana",
        "xrp": "ripple",
        "ada": "cardano"
    }

    coin_id = mapping.get(coin_name, coin_name)

    price = get_price(coin_id)

    if price:
        await update.message.reply_text(f"💰 {coin_name.upper()} narxi: ${price}")
    else:
        await update.message.reply_text("❌ Coin topilmadi. Masalan: /price btc")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("🚀 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
