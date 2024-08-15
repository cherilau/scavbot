from common import * 
from telegram import InputMediaPhoto

async def show_all(update: Update, context: CallbackContext):
    reply_keyboard = [
        ["🗺️ Show Map", "🧩 Show Riddles"],
        ["🧸 Show Items", "📸 Show Photos"],
        ["⏪ Go Back"]
    ]
    await update.message.reply_text("Need a refresher of what to do? We got you.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard)
    )

async def go_back(update: Update, context: CallbackContext):
    await update.message.reply_text(
        random.choice(tips),
        reply_markup=ReplyKeyboardMarkup(default_reply_keyboard)
    )


async def map(update: Update, context: CallbackContext):
    await update.message.reply_photo("images/scav_map.jpg", "Here's the map, your guide to see,\nEverything you need is within the boundary.")

async def riddles(update: Update, context: CallbackContext):
    await update.message.reply_text(
        """
<i>[100 points each]</i>
Crack each riddle, claim your prize,
100 points before your eyes.

<b>RIDDLE #1</b>
<blockquote>Outside the school where lawyers train,
runs a street with no lanes. 
Read the signs and you will see,
The fruit - _ _ _ _ _ _  _ _ _ _ _ you seek, adds fragrance and acidity to curries.</blockquote>

<b>RIDDLE #2</b> 
<blockquote>On the same road as Singapore's oldest fire station.
Stands a building full of history and colour
Walk along the side and read about the bridges of this nation
The one you seek, is named after Straits Settlements first governor,
 _ _ _  _ _ _ _ _ _</blockquote>

<b>RIDDLE #3</b> 
<blockquote>On top of a mall built for tech,
lies a farm of freshly grown vege.
If you observe with care and zest,
Amid grey and white, find your quest.
Hidden in "white" is what you seek.
_ _ _ _ _  _ _ _ _</blockquote>

<b>RIDDLE #4</b> 
<blockquote>There’s a five-star hotel along the river.
Go inside, and underneath, and discover,
you will see what used to be.
Marked by milestone 14 1/2, _ _ _ _ _ _  _ _ _ _, it shall be.</blockquote>

<b>RIDDLE #5</b> 
<blockquote>Near a museum where designs and innovation takes flight,
A toucan playground brings joy and light.
Once drab, now a colourful delight,
_ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ 
Authority made it right.</blockquote>

        """, 
        parse_mode = "HTML"

    )

async def items(update: Update, context: CallbackContext):
     await update.message.reply_text(
        """
<i>[10 points each]</i>
Snap a pic with each city find,
Ten items total, keep them in mind!\n
1. E-bike
2. Recycling Blue Bins 
3. Public bicycle pump ready for use
4. Lightning rod atop a building
5. Solar Panels 
6. CCTV ensuring security
7. Public Bench with Charging 
8. A bus stop displaying real-time arrival timings
9. A contactless vending machine offering snacks
10. Singapore flags proudly aligned
""", parse_mode="HTML"
     )

async def photo(update: Update, context: CallbackContext):
    list_of_media = [InputMediaPhoto(media=open('images/photo_01.jpg', 'rb')),
                     InputMediaPhoto(media=open('images/photo_02.jpg', 'rb')),
                     InputMediaPhoto(media=open('images/photo_03.jpg', 'rb')),
                     InputMediaPhoto(media=open('images/photo_04.jpg', 'rb')),
                     InputMediaPhoto(media=open('images/photo_05.jpg', 'rb')),
                     InputMediaPhoto(media=open('images/photo_06.jpg', 'rb')),                     
                     InputMediaPhoto(media=open('images/photo_07.jpg', 'rb')),
                     InputMediaPhoto(media=open('images/photo_08.jpg', 'rb')),
                ]

    await update.message.reply_media_group(list_of_media, caption = "<i>[50 points each]</i>\nSeek the spot the picture's shown,\nSnap a photo of your own", parse_mode="HTML")