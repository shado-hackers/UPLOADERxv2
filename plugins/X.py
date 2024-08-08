@Client.on_message(filters.command(["privacy"]))
async def privacy(client: Client, message: Message):
    with contextlib.suppress(ReactionInvalid):
        await message.react(emoji="👀")
    try:
        botname = "@HEXAX_bot"  # Replace with your bot's name
        await message.reply_photo(
            "https://heximg.pages.dev/file/c54802b4154b1ade1b014.jpg",
            caption=(
                f"Hi {message.from_user.mention},\n\n"
                f"<b>🔴Privacy Policy For {botname}</b>\n\n"
                f"<b>📅Effective Date:</b> 15 July 2024\n\n"
                "This Privacy Policy explains how we collect, use, and protect your information when you interact with our Telegram bot designed for group management.\n\n"
                "#🗂️ Information We Collect</b>\n\n"
                "When you use our Telegram bot, we may collect the following types of information:\n"
                "- User Information,⚡Basic information such as your Telegram ID, username, and any other data you choose to provide.\n"
                "- <b>Group Information</b>: Data related to the groups you manage, including group ID, group name, and member details.\n\n"
                "<b>2.📢 How We Use Your Information</b>\n\n"
                "We use the collected information to:\n"
                "- 🌐Manage and maintain group functionalities,🔴Provide support and improve our services.⚡Communicate important updates or changes related to the bot\n"
                
                
                "<b>3.🌐 How We Protect Your Information&Sharing Your Information</b>\n\n"
                "☣️We implement various security measures to protect your information from unauthorized access, alteration, disclosure, or destruction. However, please be aware that no method of transmission over the internet or electronic storage is 100% secure📡We do not share your information with third parties.\n\n"
                
               
                "<b>6. 🗳️Changes to This Privacy Policy</b>\n\n"
                "⚠️We may update this Privacy Policy from time to time. We will notify you of any significant changes by updating the policy in the bot. It is your responsibility to review this policy periodically.\n\n"
                "<b>7. 🕵️Contact Us</b>\n\n"
                "If you have any questions or concerns about this Privacy Policy or our practices, please contact us my owner."
            )
        )
    except (ChatSendPlainForbidden, ChatSendPhotosForbidden):
        await client.send_message(
            "LOG_GROUP", 
            f"❗️ <b>WARNING</b>\nI'm leaving from {message.chat.id} since I didn't have sufficient admin permissions."
        )
        await message.chat.leave()
