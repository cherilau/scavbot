from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes, MessageHandler, ConversationHandler, filters
import random

default_reply_keyboard = [
    ["🔍 Get a Hint"],
    ["👁️ Show Mission Brief"],
    ["🙋🏻 Answer a Riddle", "🎯 Check Progress"],
    ["🆘 Help", "🏙️ About"]
    
]