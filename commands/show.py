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
        f"Going back!\n\n{random.choice(tips)}",
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
The fruit - _ _ _ _ _ _   _ _ _ _ _ you seek, adds fragrance and acidity to curries.</blockquote>

<b>RIDDLE #2</b> 
<blockquote>On the same road as Singapore's oldest fire station.
Stands a building full of history and colour
Walk along the side and read about the bridges of this nation
The one you seek, is named after Straits Settlements first governor,
 _ _ _   _ _ _ _ _ _</blockquote>

<b>RIDDLE #3</b> 
<blockquote>On top of a tech mall where the future's bright,
In a realm of grey and white, your quest takes flight.
On one of two rooftops, a farm you will find,
Accessible by staircase, where fresh veggies unwind.
Hidden within "white" is what you seek.
_ _ _ _ _   _ _ _ _</blockquote>

<b>RIDDLE #4</b> 
<blockquote>There’s a five-star hotel along the river.
Go inside, and underneath, and discover,
Near a red post, you will see what used to be
Marked by milestone 14 1/2, _ _ _ _ _ _   _ _ _ _, it shall be.</blockquote>

<b>RIDDLE #5</b> 
<blockquote>Near the scenic bay where modern landmarks soar high,
A museum's close by, and a toucan playground catchs the eye
Once drab, now a colourful delight,
_ _ _ _ _   _ _ _ _ _ _ _ _ _ _ _ _ _ 
Authority made it right.</blockquote>

        """, 
        parse_mode = "HTML"

    )

async def items(update: Update, context: CallbackContext):
     await update.message.reply_text(
        """
🎯 (10 points each) 🎯

Snap a pic with each of these city finds—10 items in total. Keep your eyes peeled and your camera ready!

1. 🚲 E-bike
2. ♻️ Recycling Blue Bins
3. 🚿 Public bicycle pump ready for use
4. ⚡️ Lightning rod atop a building
5. ☀️ Solar Panels
6. 🎥 CCTV camera ensuring security
7. ⚡️ Public Bench with Charging
8. 🚌 A bus stop displaying real-time arrival timings
9. 🍫 A contactless vending machine offering snacks
10. 🇸🇬 Singapore flags proudly aligned

Good luck and have fun hunting! 🌟📸
""", 
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