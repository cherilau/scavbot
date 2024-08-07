from common import * 

async def start(update: Update, context: CallbackContext):
    reply_keyboard = [
        ["🔍 Get a Hint"],
        ["🗺️ Show Map", "🧩 Show Riddles"],
        ["🙋🏻 Answer a Riddle"],
        ["🗣️ Talk to the Game Master"]
    ]

    await update.message.reply_text(
        "Hi! Welcome. [insert more message here]",
        # reply_markup=InlineKeyboardMarkup(keyboard),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard)
    )