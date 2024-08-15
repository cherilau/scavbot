from common import * 

async def start(update: Update, context: CallbackContext):
    reply_keyboard = [
        ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
        ["🗺️ Show Map", "🧩 Show Riddles"],
        ["🧸 Show Items", "📸 Show Photos"],
        ["🗣️ Talk to the Game Master"]
    ]

    await update.message.reply_text(
        "Hi! Welcome. [insert more message here]",
        # reply_markup=InlineKeyboardMarkup(keyboard),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard)
    )

async def quit(update: Update, context: CallbackContext):
    reply_keyboard = [
        ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
        ["🗺️ Show Map", "🧩 Show Riddles"],
        ["🧸 Show Items", "📸 Show Photos"],
        ["🗣️ Talk to the Game Master"]
    ]

    await update.message.reply_text(
        "The process has been stopped.",
        # reply_markup=InlineKeyboardMarkup(keyboard),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard)
    )

    return -1