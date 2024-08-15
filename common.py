from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes, MessageHandler, ConversationHandler, filters
import random

default_reply_keyboard = [
    ["🔍 Get a Hint"],
    ["👁️ Show Mission Brief"],
    ["🙋🏻 Answer a Riddle", "🎯 Check Progress"],
    ["🗣️ Talk to the Game Master", "🏙️ About"]
]

tips = [ # a fun easter egg (mainly because i need to say something to make sure the keyboard shows up)
    "Tip: Use /help to see more commands.", 
    "Tip: Use /help to see more commands.", 
    "Tip: Use /help to see more commands.", 
    "Tip: Click back in and out for a random tip!",
    "Tip: If the keyboard ever stops showing up, /quit or /start usually does the trick.",
    "Tip: Both inline buttons and slash commands can be used.",
    "Tip: Both inline buttons and slash commands can be used.",
    "Tip: This bot can be used in both group chats and DMs — you can even switch around!",
    "Tip: This bot can be used in both group chats and DMs — you can even switch around!",
    "Tip: Check out the menu button.", # menu button has not been set up
    "Tip: Hints don't affect your points.",
    "Tip: The time you first answer each riddle is being recorded. Zoom zoom!",
]

# default_reply_keyboard_old = [
#     ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
#     ["🗺️ Show Map", "🧩 Show Riddles"],
#     ["🧸 Show Items", "📸 Show Photos"],
#     ["🗣️ Talk to the Game Master"]
# ]
# for reference
# await update.message.reply_text(
#     "string to send here", 
#     reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
# )