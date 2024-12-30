from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

# Help Buttons Layout
HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🛠 Mise", callback_data="mise"),
            InlineKeyboardButton("🤖 AI", callback_data="ai"),
        ],
        [
            InlineKeyboardButton("💻 Device", callback_data="device"),
            InlineKeyboardButton("🛠️ Tools", callback_data="tools"),
        ],
        [
            InlineKeyboardButton("🖥️ System", callback_data="system"),
            InlineKeyboardButton("🔍 Search", callback_data="search"),
            InlineKeyboardButton("📖 Dictionary", callback_data="dictionary"),
        ],
        [
            InlineKeyboardButton("🌐 General", callback_data="general"),
            InlineKeyboardButton("🗺️ Maps", callback_data="maps"),
        ],
        [
            InlineKeyboardButton("🔧 Utilities", callback_data="utilities"),
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="back"),
            InlineKeyboardButton("❌ Close", callback_data="close"),
        ],
    ]
)

# Define the HELP_TEXT here
HELP_TEXT = """<b>Welcome to the Bot Help Menu!</b>
Here are the features and commands available:

<b>Main Features:</b>
- 🛠 Mise
- 🤖 AI
- 💻 Device
- 🛠️ Tools
- 🖥️ System
- 🔍 Search
- 📖 Dictionary
- 🌐 General
- 🗺️ Maps
- 🔧 Utilities

Use the buttons below to explore more categories."""

@Client.on_message(filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )

@Client.on_callback_query()
async def handle_callback_query(bot, update):
    data = update.data

    if data == "mise":
        await update.edit_message_text(
            text="""<b>Help: Extra Modules</b>
<b>Note:</b> These are additional features available in the bot.

<b>Commands and Usage:</b>
• /id - Get the ID of a specific user.
• /info - Get information about a user.
• /imdb - Get film information from IMDb.
• /search - Get film information from various sources.

<b>AI Tools:</b>
• /gojo <query> - Use Gojo AI (supports photos & stickers).
• /gpt <query> - Get a response from ChatGPT.
• /groq <query> - Get a response from Groq AI.
• /google or /gemini <query> - Get a response from Gemini AI PRO.

<b>Image Generation:</b>
• /draw <query> - Generate an image from a text description.
• /imagine <query> - Generate an image from a text description.
• /art <query> - Generate an artistic image from text.
• /bdraw <query> - Generate an image using the Blackbox model.
            """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back", callback_data="back")]]
            ),
            disable_web_page_preview=True
        )
    elif data == "search":
        await update.edit_message_text(
            text="""<b>Help: Search Tools</b>
<b>Note:</b> Use these commands to perform searches for various categories.

<b>Commands and Usage:</b>
• /google <query> - <code>Search on Google.</code>
• /bing <query> - <code>Search on Bing.</code>
• /yahoo <query> - <code>Search on Yahoo.</code>
• /wiki <query> - <code>Search on Wikipedia.</code>
• /youtube <query> - <code>Search for videos on YouTube.</code>
            """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back", callback_data="back")]]
            ),
            disable_web_page_preview=True
        )
    elif data == "ai":
        await update.edit_message_text(
            text="""<b>Help: AI Tools</b>
<b>Note:</b> The AI tools are used to get responses from various AI sources.

<b>Commands and Usage:</b>
• /gojo <query> - <code>Use Gojo AI (photos & stickers).</code>
• /gpt <query> - <code>Get a response from ChatGPT.</code>
• /groq <query> - <code>Get a response from Groq AI.</code>
• /google or /gemini <query> - <code>Get a response from Gemini AI PRO.</code>
            """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back", callback_data="back")]]
            ),
            disable_web_page_preview=True
        )
    elif data == "device":
        await update.edit_message_text(
            text="""<b>Help: Device Tools</b>
<b>Note:</b> These commands help you retrieve device-related information.

<b>Commands and Usage:</b>
• /deviceinfo <device_name> - <code>Get detailed information about a device.</code>
• /specs <device_name> - <code>Fetch specifications for a device.</code>
• /compare <device1> <device2> - <code>Compare two devices.</code>
            """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back", callback_data="back")]]
            ),
            disable_web_page_preview=True
        )
    elif data == "tools":
        await update.edit_message_text(
            text="""<b>Help: Tools</b>
<b>Note:</b> These are utility tools available in the bot.

<b>Commands and Usage:</b>
• /calculator <expression> - <code>Perform calculations directly in chat.</code>
• /convert <value> <unit> - <code>Convert units (e.g., cm to inches).</code>
• /qr <text> - <code>Generate a QR code for the given text.</code>
• /barcode <text> - <code>Generate a barcode for the given text.</code>
• /shorten <url> - <code>Shorten a given URL using a URL shortener service.</code>
            """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back", callback_data="back")]]
            ),
            disable_web_page_preview=True
        )
    elif data == "back":
        await update.edit_message_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS
        )
    elif data == "close":
        await update.message.delete()
    else:
        await update.answer("❗ Invalid option selected!", show_alert=True)
