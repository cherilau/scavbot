from common import *
from database import *
from datetime import datetime

global num
num = 0

CHOOSING, ANSWER = range(2)

async def check_progress(update: Update, context: CallbackContext):

    sql_statement = '''
        select * from timestamp t, user u 
        where u.username = t.user
        and u.group_name = (select group_name from user where username = '{user}');
    '''.format(num=num, user=update.message.from_user["username"])
    results = fetch_many(sql_statement)
    list_of_completed = []
    for dict in results:
        if dict["riddle"] not in list_of_completed:
            list_of_completed.append(dict["riddle"])
    str_to_present = "Here's your current progress.\n\n"
    for i in range(1,6): # hardcoded for 5 questions, can be replaced by one select count(*) of riddle
        str_to_present += f"Question {i}: "
        if i in list_of_completed:
            str_to_present += "✅"
        else:
            str_to_present += "❓"
        str_to_present += "\n"

    if len(list_of_completed) == 5: # hardcoded, all complete
        str_to_present += "\nYou're all done! Good job!"
    else:
        num_left = 5 - len(list_of_completed)
        str_to_present += f"\n{num_left} left. Keep up the good work!"

    await update.message.reply_text(str_to_present, 
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )
    


async def choose_answer(update: Update, context: CallbackContext):
    # check if verified first
    if ('verified' not in context.user_data):
        user = update.message.from_user["username"]
        if fetch_one(f"select * from user where username = '{user}';") != None:
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
        # get from database, see if answered yet
        
        sql_statement = '''
        select * from timestamp t, user u 
        where u.username = t.user
        and t.riddle = {num}
        and u.group_name = (select group_name from user where username = '{user}');
        '''.format(num=num, user=update.message.from_user["username"])

        result = fetch_one(sql_statement)
        if result == None:
            await update.message.reply_text(
                f"What is your answer for riddle {num}?",
                reply_markup=ReplyKeyboardRemove()
            )
            return ANSWER
        else: 
            # check if it's by user or by user's teammate
            if result['user'] == update.message.from_user["username"]:
                await update.message.reply_text(
                    "You have already answered this question.",
                    reply_markup = ReplyKeyboardMarkup(default_reply_keyboard))
            else: 
                await update.message.reply_text(
                    f"This question has already been answered by your team member, @{result['user']}",
                    reply_markup = ReplyKeyboardMarkup(default_reply_keyboard))

            return ConversationHandler.END

async def answer(update: Update, context: CallbackContext):
    # answer_list = ["", "kaffir limes","ORD BRIDGE","Urban Farm","Jurong Road","Urban Redevelopment"]
    if ('answer_list' not in context.user_data):
        answer_list = [""]
        result_list = fetch_many("select * from riddle order by num asc;")
        for result in result_list:
            answer_list.append(result['answer'])
        context.user_data['answer_list'] = answer_list
    else:
        answer_list = context.user_data['answer_list']
        
    if update.message.text.lower().strip() == answer_list[num].lower():
        await update.message.reply_text(
            f"_{answer_list[num]}_ is correct\!",
            reply_markup=ReplyKeyboardMarkup(default_reply_keyboard),
            parse_mode = "MarkdownV2" # give back the options from start
        )
        # insert database stuff here, only if correct
        username = update.message.from_user["username"]
        cur_time = datetime.now()

        if fetch_one("select * from timestamp where riddle = '{riddle}' and user = '{user}'".format(riddle = num, user = username)) != None:
            await update.message.reply_text(
                "You have already answered this question correctly! Use /check_progress to see more!"
            )
        else:
            sql_statement = "insert into timestamp (riddle, user, timestamp) values ('{riddle}', '{user}', '{timestamp}');"\
                            .format(riddle = num, user = username, timestamp = cur_time)
            try:
                execute_sql_statement(sql_statement)
            except mysql.connector.Error as e:
                if e.errno == 1644:
                    await update.message.reply_text(
                        "A group member has already answered this question! Use /check_progress to see more!"
                    )

        return ConversationHandler.END

    else:
        await update.message.reply_text(
            f"_{update.message.text}_ is incorrect\!\n\nHint: Check if the number of characters match\.",
            reply_markup=ReplyKeyboardMarkup(default_reply_keyboard),
            parse_mode = "MarkdownV2" # give back the options from start
        )
    
        return ConversationHandler.END # either way the convo ends here. will have to go back to answer a riddle to start again


async def no_answer(update: Update, context: CallbackContext):
    # for when they click answer then back
    await update.message.reply_text(
        "Alright!",
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
        )
    return ConversationHandler.END