from common import *

async def contact(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Want to talk to the game master? No problem!\n\n"
        "For riddles, message @cloewhat.\n"
        "For photos, message @changheng1."
    )