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
from commands.answer import *

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
    app.add_handler(CommandHandler("riddles", riddles)) # sends the riddles
    app.add_handler(CommandHandler("items", items)) # sends the map
    app.add_handler(CommandHandler("photo", photo)) # sends the riddles
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
    app.add_handler(MessageHandler(filters.Regex("🗣️ Talk to the Game Master"), contact))
    app.add_handler(MessageHandler(filters.Regex("🧸 Show Items"), item))    
    app.add_handler(MessageHandler(filters.Regex("📸 Show Photos"), photo))

    # this entire thing is for the answer 
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("answer", choose_answer), MessageHandler(filters.Regex("🙋🏻 Answer a Riddle"), choose_answer)],
        states={
            CHOOSING: [
                MessageHandler(filters.Regex("^Riddle [1-5]$"), ask_for_answer),
            ],
            ANSWER: [
                MessageHandler(
                    filters.TEXT, answer
                )
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^↩️ Back$"), no_answer)],
    )

    app.add_handler(conv_handler)
    

    # Run the bot until the user presses Ctrl-C
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()