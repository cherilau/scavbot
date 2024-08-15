from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes, MessageHandler, ConversationHandler, filters


default_reply_keyboard = [
    ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
    ["🗺️ Show Map", "🧩 Show Riddles"],
    ["🧸 Show Items", "📸 Show Photos"],
    ["🗣️ Talk to the Game Master"]
]