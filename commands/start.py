from common import * 

# start, quit, about, help, commands, contact

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome to the Smart City Society Scavenger Hunt! 🎉 We’re thrilled to have you join us.\n\nThis bot is your ultimate guide for today’s adventure. Whether you need hints 🕵️‍♂️, want to review the mission brief 📜, or need help with riddles 🧩, we’ve got you covered! Explore the inline keyboard or use the /help command to discover all available options. If you run into any technical issues, please DM @cherilau on Telegram.\n\nHave a fantastic time hunting! 🚀🔍",
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )
    # await update.message.reply_text("test")

async def quit(update: Update, context: CallbackContext):
    # used to quit conversations
    await update.message.reply_text(
        "The process has been stopped.",
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )
    return -1

async def about(update: Update, context: CallbackContext):
    # used to quit conversations
    scs_inline_keyboard = [[InlineKeyboardButton(text="SCS Telegram Channel", url="https://t.me/+nF70h9d7ljE1OGFl")],
                           [InlineKeyboardButton(text="SCS Membership Form", url = "https://forms.gle/WE9jEtmM8D43w64H6")]
                          ]
    await update.message.reply_text(
        "Smart City Society is a student-led organization dedicated to exploring Smart Cities and the innovative technologies that tackle urbanization challenges and enhance the quality of life for all residents. 🌆✨\n\nWe regularly host networking sessions 🤝, industry talks 🎤, and an exciting annual hackathon 💡. Join us to connect, learn, and innovate! 🚀",
        reply_markup= InlineKeyboardMarkup(scs_inline_keyboard), 
    )
    # await update.message.reply_text(
    #     "We'll look forward to have you!",
    #     reply_markup= ReplyKeyboardMarkup(default_reply_keyboard), 
    # )

async def help(update: Update, context: CallbackContext):
    # used to quit conversations
    await update.message.reply_text(
        '''
Use /commands to pull up a full list of slash commands. 

If you need help with the riddles, try /hint instead!

To talk to the game master, message @cloewhat on Telegram.\n
If you face any technical difficulties with the bot, message @cherilau on Telegram."
''',
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )
    return -1

async def commands(update: Update, context: CallbackContext):
    await update.message.reply_text(
        '''
/hint: get a hint
/map: show the map
/riddles: show all 5 riddles
/items: show the list of items to find
/photo: show all photo spots to find
/answer: answer a riddle
/verify: verify yourself to be able to answer riddles
/contact: message the game master
/check_progress: see what riddles you or your teammates have answered
/about: learn more about SCS!
''',
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
)
    return -1

async def contact(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Want to talk to the game master? No problem! Message @cloewhat!"
    )