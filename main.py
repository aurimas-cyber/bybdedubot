from telegram.ext import MessageHandler, CallbackQueryHandler, filters

# Callback kai paspaudžiamas mygtukas "Ask AI"
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Send your question to AI.")

# Handleris tekstinėms žinutėms
async def handle_message(update: Update, context: CallbackContext):
    response = generate_ai_response(update.message.text)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))  # 👈 šitas prideda mygtuko veikimą
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # 👈 šitas leidžia rašyt tekstą
    print("Bot is running...")
    app.run_polling()

import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters,
)
from ai_engine.logic import generate_ai_response

# Tavo token'as tiesiogiai įrašytas (tik dev stadijai — deploy metu naudok .env)
BOT_TOKEN = "8348255481:AAEu5gWdflKy8a2IgjK5JqGKkc34RYlPUIc"

async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Ask AI", callback_data='ask_ai')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome to BybdeduBot! Choose:', reply_markup=reply_markup)

async def ask(update: Update, context: CallbackContext):
    await update.message.reply_text("Send your question to AI.")

async def handle_message(update: Update, context: CallbackContext):
    response = generate_ai_response(update.message.text)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
