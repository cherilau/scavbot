from common import * 

async def map(update: Update, context: CallbackContext):
    await update.message.reply_photo("scav_map.jpg", "Here's the map!")

async def riddles(update: Update, context: CallbackContext):
    await update.message.reply_text(
        # "**RIDDLE #1**\n"
        # "Outside the school where lawyers train,\n"
        # "runs a street with no lanes.\n"
        # "Read the signs and you will see,\n"
        # "The fruit - _ _ _ _ _ _  _ _ _ _ _ you seek, adds fragrance and acidity to curries."
        """
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