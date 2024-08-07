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


# choose_hint_photo
async def choose_hint_photo(update: Update, context: CallbackContext):
    inline_photo_keyboard = [
        [InlineKeyboardButton("Photo 1", callback_data="photo 1"), InlineKeyboardButton("Photo 2", callback_data="photo 2")],
        [InlineKeyboardButton("Photo 3", callback_data="photo 3"), InlineKeyboardButton("Photo 4", callback_data="photo 4")],
        [InlineKeyboardButton("Photo 5", callback_data="photo 5"), InlineKeyboardButton("Photo 6", callback_data="photo 6")],
        [InlineKeyboardButton("Photo 7", callback_data="photo 7"), InlineKeyboardButton("Photo 8", callback_data="photo 8")],
        [InlineKeyboardButton("↩️ Back", callback_data="hint")],
    ]
    
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="Which photo do you need help with?", 
        reply_markup=InlineKeyboardMarkup(inline_photo_keyboard))


async def show_hint_photo(update: Update, context: CallbackContext):
    back_keyboard = [[InlineKeyboardButton("↩️ Back", callback_data="hint")]]

    hint_photo_dict = {
        "photo 1": "In front of the Peranakan Museum",
        "photo 2": "Basement of Fullerton Hotel",
        "photo 3": "Funan B2 Bicycle Parking",
        "photo 4": "Funan Green Rooftop",
        "photo 5": "Fullerton Hotel Entrance",
        "photo 6": "Fullerton Hotel Basement",
        "photo 7": "In front of Sir Stamford Raffles Statue",
        "photo 8": "OUE Building"
    }

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text= f"Hint for {query.data}: ||{hint_photo_dict[query.data]}||",
        reply_markup=InlineKeyboardMarkup(back_keyboard),
        parse_mode = "MarkdownV2")