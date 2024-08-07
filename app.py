from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes, MessageHandler, ConversationHandler, filters
# import re
import logging
import os
from dotenv import load_dotenv

# importing all the code i've put in a folder for no other reason than cleaniness and visual pleasure
from commands.contact import *
from commands.hint import *
from commands.show import *
from commands.start import *

logging.basicConfig(
    format = '%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s',
    level = logging.INFO
)

logger = logging.getLogger(__name__)

load_dotenv("./.env")
TOKEN = os.getenv("token")


def main():
    # updater = Updater(TOKEN)
    # dp = updater.dispatcher
    app = Application.builder().token(TOKEN).build()

    # slash commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hint", hint))
    app.add_handler(CommandHandler("map", map)) # sends the map
    app.add_handler(CommandHandler("riddles", riddles)) # sends the map
    # app.add_handler(CommandHandler("answer", answer)) 
    app.add_handler(CommandHandler("contact", contact)) 

    # callback commands for hint
    app.add_handler(CallbackQueryHandler(hint, pattern='hint'))
    app.add_handler(CallbackQueryHandler(choose_hint_riddle, pattern='^riddle$'))
    app.add_handler(CallbackQueryHandler(show_hint_riddle, pattern='^riddle [1-5]$'))
    app.add_handler(CallbackQueryHandler(choose_hint_photo, pattern='^photo$'))
    app.add_handler(CallbackQueryHandler(show_hint_photo, pattern='^photo [1-8]$'))

    # inline button commands
    app.add_handler(MessageHandler(filters.Regex("🔍 Get a Hint"), hint))    
    app.add_handler(MessageHandler(filters.Regex("🗺️ Show Map"), map))
    app.add_handler(MessageHandler(filters.Regex("🧩 Show Riddles"), riddles))    
    # app.add_handler(MessageHandler(filters.Regex("🙋🏻 Answer a Riddle"), answer))
    app.add_handler(MessageHandler(filters.Regex("🗣️ Talk to the Game Master"), contact))    

    # dp.add_handler(MessageHandler(Filters.text, start))

    # Run the bot until the user presses Ctrl-C
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()