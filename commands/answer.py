from common import *

global num
num = 0

CHOOSING, ANSWER = range(2)

async def choose_answer(update: Update, context: CallbackContext):
    inline_riddle_keyboard = [
        [InlineKeyboardButton("Riddle 1", callback_data="answer 1"), InlineKeyboardButton("Riddle 2", callback_data="answer 2")],
        [InlineKeyboardButton("Riddle 3", callback_data="answer 3"), InlineKeyboardButton("Riddle 4", callback_data="answer 4")],
        [InlineKeyboardButton("Riddle 5", callback_data="answer 5"), InlineKeyboardButton("↩️ Back", callback_data="answer")],
    ]

    reply_keyboard = [
        ["Riddle 1", "Riddle 2"],
        ["Riddle 3", "Riddle 4"],
        ["Riddle 5", "↩️ Back"]
    ]

    if update.message == None:
        # query = update.callback_query
        # await query.answer()
        await update.callback_query.edit_message_text(
            "What riddle would you like to answer?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    else: 
        await update.message.reply_text(
            "What riddle would you like to answer?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    
    return CHOOSING


async def ask_for_answer(update: Update, context: CallbackContext):
    global num
    if update.message.text[-1] in ["1", "2", "3", "4", "5"]:
        num = int(update.message.text[-1])
        await update.message.reply_text(
                f"What is your answer for riddle {num}?",
                reply_markup=ReplyKeyboardRemove()
            )
        return ANSWER

    # else: # actually this will never get here because of regex
    #     # shove them back to choosing a question
    #     reply_keyboard = [["Riddle 1", "Riddle 2"],["Riddle 3", "Riddle 4"], ["Riddle 5", "↩️ Back"]]
    #     await update.message.reply_text(
    #         "What riddle would you like to answer?",
    #         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    #     )
    #     return CHOOSING


async def answer(update: Update, context: CallbackContext):
    answer_list = ["", "kaffir limes","ORD BRIDGE","Urban Farm","Jurong Road","Urban Redevelopment"]
    if num < 6 and num > 0:
        reply_keyboard = [["🔍 Get a Hint"],["🗺️ Show Map", "🧩 Show Riddles"],["🙋🏻 Answer a Riddle"],["🗣️ Talk to the Game Master"]]
        # check if answer matches
        if update.message.text.lower().strip() == answer_list[num].lower():
             await update.message.reply_text(
                f"_{answer_list[num]}_ is correct\!",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard),
                parse_mode = "MarkdownV2" # give back the options from start
        )
        else:
            await update.message.reply_text(
                f"_{update.message.text}_ is incorrect\!\n\nHint: Check if the number of characters match\.",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard),
                parse_mode = "MarkdownV2" # give back the options from start
            )
        
        return ConversationHandler.END # either way the convo ends here. will have to go back to answer a riddle to start again

      
    else: # should never get here. but just in case...
        reply_keyboard = [["Riddle 1", "Riddle 2"],["Riddle 3", "Riddle 4"],["Riddle 5", "↩️ Back"]]
        await update.message.reply_text(
            "What riddle would you like to answer?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard)
            )
        return CHOOSING


async def no_answer(update: Update, context: CallbackContext):
    # for when they click answer then back
    reply_keyboard = [["🔍 Get a Hint"],["🗺️ Show Map", "🧩 Show Riddles"],["🙋🏻 Answer a Riddle"],["🗣️ Talk to the Game Master"]]
    await update.message.reply_text(
        "I'll be waiting! In the meantime, here are some other options.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard)
        )
    return ConversationHandler.END