from common import *
from database import check_if_exists

global num
num = 0

CHOOSING, ANSWER = range(2)

async def choose_answer(update: Update, context: CallbackContext):

    # check if verified first
    if ('verified' not in context.user_data):
        user = update.message.from_user["username"]
        if check_if_exists(f"select * from user where username = '{user}';") == True:
            context.user_data['verified'] = True
        else:
            await update.message.reply_text(
            "You have not been verified! Use /verify before you start answering riddles.")
            return ConversationHandler.END
        

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
        reply_keyboard = [
            ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
            ["🗺️ Show Map", "🧩 Show Riddles"],
            ["🧸 Show Items", "📸 Show Photos"],
            ["🗣️ Talk to the Game Master"]
        ]
        # check if answer matches
        # await update.message.reply_text(update.message.text)

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
    reply_keyboard = [
        ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
        ["🗺️ Show Map", "🧩 Show Riddles"],
        ["🧸 Show Items", "📸 Show Photos"],
        ["🗣️ Talk to the Game Master"]
    ]

    await update.message.reply_text(
        "I'll be waiting! In the meantime, here are some other options.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard)
        )
    return ConversationHandler.END