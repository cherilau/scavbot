from common import * 

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Hi! Welcome. [insert more message here]",
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )

async def quit(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "The process has been stopped.",
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )

    return -1