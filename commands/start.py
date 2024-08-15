from common import * 

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome to Smart City Society's Scavenger Hunt! We're excited to have you here.\n\nUse this bot to help you along your journey today. Getting hints, looking at the mission brief, answering riddles — we got it all!\n\nUse the inline keyboard or /help to see the slash commands available. For any technical difficulties, DM @cherilau on telegram. Have fun!",
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
        "Smart City Society is a student focusing on Smart Cities and its related technologies that help solve urbanisation problems and improve the quality of life of all inhabitants. Our regular events include networking sessions, industry talks, and an annual hackathon.",
        reply_markup= InlineKeyboardMarkup(scs_inline_keyboard), 
    )
    # await update.message.reply_text(
    #     "We'll look forward to have you!",
    #     reply_markup= ReplyKeyboardMarkup(default_reply_keyboard), 
    # )

async def help(update: Update, context: CallbackContext):
    # used to quit conversations
    await update.message.reply_text(
        "insert help here",
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )
    return -1