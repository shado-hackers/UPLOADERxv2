from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

# Initialize the bot
app = Client("my_bot")

# Define HELP_BUTTONS with emoji support
HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📝 Mise", callback_data="mise"),
            InlineKeyboardButton("🖼️ ImgEdit", callback_data="imgeedit"),
            InlineKeyboardButton("🔍 Search", callback_data="search"),
        ],
        [
            InlineKeyboardButton("📋 Paste", callback_data="paste"),
            InlineKeyboardButton("⚙️ Extra", callback_data="extra"),
            InlineKeyboardButton("🤖 AI", callback_data="ai"),
        ],
        [
            InlineKeyboardButton("📱 Device", callback_data="device"),
            InlineKeyboardButton("📚 Dictionary", callback_data="dictionary"),
            InlineKeyboardButton("🔧 Utilities", callback_data="utilities"),
        ],
    ]
)

# Command to show the help menu
@app.on_message(filters.command("help") & filters.private)
async def show_help(client, message: Message):
    await message.reply(
        "Choose a category from the help menu below 👇:",
        reply_markup=HELP_BUTTONS
    )

# Callback query handler for the "Paste" button
@app.on_callback_query(filters.regex("^paste$"))
async def paste_help(client, callback_query: CallbackQuery):
    text = """<b>Help: Paste Feature 📋</b>
<b>Note:</b> The Paste feature allows you to quickly paste and share various content.

<b>Commands and Usage:</b>
• /paste <text> - <code>Paste text into the chat.</code>
• /paste link <url> - <code>Share a link as pasted content.</code>
• /paste file <file_name> - <code>Upload a file as pasted content.</code>
"""
    await callback_query.message.edit(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]  # Back button to return to the help menu
        )
    )

# Callback query handler for the "Mise" button
@app.on_callback_query(filters.regex("^mise$"))
async def mise_help(client, callback_query: CallbackQuery):
    text = """<b>Help: Mise Feature 📝</b>
<b>Note:</b> The Mise feature allows you to manage your mise tasks efficiently.

<b>Commands and Usage:</b>
• /mise <task> - <code>To start a new mise task.</code>
• /mise status - <code>To check the status of your current task.</code>
• /mise cancel - <code>To cancel an ongoing task.</code>
"""
    await callback_query.message.edit(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]  # Back button to return to the help menu
        )
    )

# Callback query handler for the "AI" button
@app.on_callback_query(filters.regex("^ai$"))
async def ai_help(client, callback_query: CallbackQuery):
    text = """<b>Help: AI Tools 🤖</b>
<b>Note:</b> The AI tools are used to get responses from various AI sources.

<b>Commands and Usage:</b>
• /gojo <query> - <code>Use Gojo AI (photos & stickers).</code>
• /gpt <query> - <code>Get a response from ChatGPT.</code>
• /groq <query> - <code>Get a response from Groq AI.</code>
• /google or /gemini <query> - <code>Get a response from Gemini AI PRO.</code>
"""
    await callback_query.message.edit(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]  # Back button to return to the help menu
        )
    )

# Callback query handler for the "Device" button
@app.on_callback_query(filters.regex("^device$"))
async def device_help(client, callback_query: CallbackQuery):
    text = """<b>Help: Device Information 📱</b>
<b>Note:</b> Use this feature to get information about various devices, specifications, and comparisons.

<b>Commands and Usage:</b>
• /device <model> - <code>Get details about a device.</code>
• /compare <device1> <device2> - <code>Compare two devices.</code>
"""
    await callback_query.message.edit(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]  # Back button to return to the help menu
        )
    )

# Callback query handler for the "Dictionary" button
@app.on_callback_query(filters.regex("^dictionary$"))
async def dictionary_help(client, callback_query: CallbackQuery):
    text = """<b>Help: Dictionary Feature 📚</b>
<b>Note:</b> Use this feature to search for word definitions and translations.

<b>Commands and Usage:</b>
• /define <word> - <code>Get the definition of a word.</code>
• /translate <word> - <code>Translate a word into another language.</code>
"""
    await callback_query.message.edit(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]  # Back button to return to the help menu
        )
    )

# Callback query handler for the "Utilities" button
@app.on_callback_query(filters.regex("^utilities$"))
async def utilities_help(client, callback_query: CallbackQuery):
    text = """<b>Help: Utilities Tools 🔧</b>
<b>Note:</b> Use various tools to perform calculations, conversions, and more.

<b>Commands and Usage:</b>
• /calculator <expression> - <code>Perform a calculation.</code>
• /convert <value> <unit1> <unit2> - <code>Convert units (e.g., km to miles).</code>
"""
    await callback_query.message.edit(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]  # Back button to return to the help menu
        )
    )

# Callback query handler for other help sections
@app.on_callback_query(filters.regex("^(paste|extra)$"))
async def help_callback(client, callback_query: CallbackQuery):
    data = callback_query.data

    if data == "paste":
        text = "Paste: Here is how to use the paste feature."
    elif data == "extra":
        text = "Extra: Here are additional features."

    await callback_query.message.edit(
        text=text,
        reply_markup=HELP_BUTTONS  # Optionally add back the buttons
    )

# Run the bot
app.run()
