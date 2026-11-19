
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN 9192094858:AAFDt1eS4HPzZkbATRZxs6SamyejL0CClZc
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selam abi, bot çalışıyor ✅")

async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Dedin ki: {update.message.text}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))
app.run_polling()
