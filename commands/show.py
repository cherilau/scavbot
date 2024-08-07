from common import * 

async def map(update: Update, context: CallbackContext):
    await update.message.reply_photo("scav_map.jpg", "Here's the map!")

async def riddles(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "chuck riddles here later"
    )