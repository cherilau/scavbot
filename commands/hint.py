from common import * 


async def hint(update: Update, context: CallbackContext):
    inline_keyboard = [
            [InlineKeyboardButton("🧩 Riddle", callback_data="riddle")],
            [InlineKeyboardButton("📸 Photo", callback_data="photo")]]

    if update.message == None:
        # query = update.callback_query
        # await query.answer()
        await update.callback_query.edit_message_text(
            "Would you like a hint for a riddle or a photo task?",
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
        )
    else: 
        await update.message.reply_text(
            "Would you like a hint for a riddle or a photo task?",
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
        )


async def choose_hint_riddle(update: Update, context: CallbackContext):
    inline_riddle_keyboard = [
        [InlineKeyboardButton("Riddle 1", callback_data="riddle 1"), InlineKeyboardButton("Riddle 2", callback_data="riddle 2")],
        [InlineKeyboardButton("Riddle 3", callback_data="riddle 3"), InlineKeyboardButton("Riddle 4", callback_data="riddle 4")],
        [InlineKeyboardButton("Riddle 5", callback_data="riddle 5"), InlineKeyboardButton("↩️ Back", callback_data="hint")],
    ]
    
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="Which riddle do you need help with?", 
        reply_markup=InlineKeyboardMarkup(inline_riddle_keyboard))


async def show_hint_riddle(update: Update, context: CallbackContext):
    back_keyboard = [[InlineKeyboardButton("↩️ Back", callback_data="hint")]]

    hint_riddle_dict = {
        "riddle 1": "Law School",
        "riddle 2": "Basement of the colourful building that is located near Clarke Quay",
        "riddle 3": "Funan",
        "riddle 4": "Fullerton Hotel ",
        "riddle 5": "Little Red Dot Museum"
    }

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text= f"Hint for {query.data}: ||{hint_riddle_dict[query.data]}||",
        reply_markup=InlineKeyboardMarkup(back_keyboard),
        parse_mode = "MarkdownV2")
