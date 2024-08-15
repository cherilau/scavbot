from common import * 
from database import *
    

GROUP, PWD = range(2)

async def verify(update: Update, context: CallbackContext):
    # get their user_id
    # check if user_id is in table of users
    # if yes, confirm the group with them and tell them who else is in the group
    # if no, start conversation handler where we ask them for group and password
    user = update.message.from_user["username"]

    if check_if_exists(f"select * from user where username = '{user}';"):
        # the user exists
        reply_keyboard = [
            ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
            ["🗺️ Show Map", "🧩 Show Riddles"],
            ["🧸 Show Items", "📸 Show Photos"],
            ["🗣️ Talk to the Game Master"]
        ]
        await update.message.reply_text("You have been verified! Go forth now.", reply_markup=ReplyKeyboardMarkup(reply_keyboard))
        return ConversationHandler.END

    else:
        await update.message.reply_text("Let's start the verification process! What is your group name?")
        return GROUP

async def group(update: Update, context: CallbackContext):
    print("now at group")
    print(f"select * from s_group where name = '{update.message.text.strip()}';")

    if check_if_exists(f"select * from s_group where name = '{update.message.text.strip()}';"):
        # group exists
        await update.message.reply_text("Got it! What's the password?")
        context.user_data["group"] = update.message.text.strip()
        return PWD
    else:
        await update.message.reply_text("Hm... I don't see a group with that name. Let's try again. \n\n<i>Hint: You should have received a message from the Game Masters with your group name and password.</i>", parse_mode = 'HTML')
        return GROUP



async def password(update: Update, context: CallbackContext):
    group_name = context.user_data["group"]
    result = return_database_results(f"select * from s_group where name = '{group_name}';")
    password = result[0]['password']

    if update.message.text.strip() == password:
        # enter user into database
        context.user_data["verified"] = True
        user = update.message.from_user
            # # User(first_name='CL', id=6008301227, is_bot=False, language_code='en', username='cherilau')

        sql_statement = '''insert into user (username, user_id, first_name, group_name) values 
                            ('{username}', {user_id}, '{first_name}', '{group_name}');'''\
                            .format(username=user['username'],user_id=user['id'],first_name=user['first_name'], group_name = group_name)
        execute_sql_statement(sql_statement)

        reply_keyboard = [
            ["🔍 Get a Hint", "🙋🏻 Answer a Riddle"],
            ["🗺️ Show Map", "🧩 Show Riddles"],
            ["🧸 Show Items", "📸 Show Photos"],
            ["🗣️ Talk to the Game Master"]
        ]
        await update.message.reply_text("You have now been verified! Go forth!", reply_markup=ReplyKeyboardMarkup(reply_keyboard))
        return ConversationHandler.END

    else:
        await update.message.reply_text("That is incorrect! Try again or use /quit to stop the verification process.")
 


    # print(result)



