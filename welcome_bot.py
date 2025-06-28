from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

BOT_TOKEN = '8115415891:AAHhC8k4L4aX8uO8z6Qp18jdvElgm_5aty0'


welcome_enabled = False
bye_enabled = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm KiraFix💡Community's happy welcome bot. I'll greet new members when they join our communiy! \n\n"
        "👋🏾❤️👨🏾‍💻 KiraFix💡Channel (https://t.me/KiraFix_tech) 🙏🏾❤️👩🏾‍💻 \n\n"
        "👋🏾❤️👨🏾‍💻 KiraFix💡Community (https://t.me/KiraFix_tech_discussion) 🙏🏾❤️👩🏾‍💻 \n\n"
        "You can use /startwelcome and /stopwelcome to control welcome messages, and /startbye and /stopbye for goodbye messages.\n"
        "Proudly made with love in Ethiopia 🇪🇹❤️"
    )

async def startwelcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global welcome_enabled
    welcome_enabled = True
    await update.message.reply_text("Welcome messages have been enabled!🍀 \n" \
    "I'll now greet new members when they join.😊")

async def stopwelcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global welcome_enabled
    welcome_enabled = False
    await update.message.reply_text("Welcome messages have been disabled.🙅🏾‍♂️🙅🏾‍♀️ \n" \
    "I won't greet new members for now.😴")

async def startbye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bye_enabled
    bye_enabled = True
    await update.message.reply_text("Goodbye messages have been enabled!💁🏾‍♂️ \n " \
    "I'll now say goodbye to members who leave.😢")

async def stopbye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bye_enabled
    bye_enabled = False
    await update.message.reply_text("Goodbye messages have been disabled.🙅🏾‍♂️🙅🏾‍♀️ \n " \
    "I won't send farewell messages for now.😴")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not welcome_enabled:
        return
    if update.message and update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            if new_member.id == context.bot.id:
                continue
            first_name = new_member.first_name
            last_name = new_member.last_name or ""
            welcome_message = (
                f"Hello {first_name} {last_name} 👋🏾, welcome to our awesome community which you are a part of now!  👨🏾‍💻👩🏾‍💻🚀 \n"
                "We're happy to have you here! Since we are on the same team, feel free to introduce yourself, join the conversation and grow with us. 📈😊 \n"
                "We believe your presence will be a blessing to the community. 🙏🏾 \n"
            )
            await update.message.chat.send_message(welcome_message)

async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not bye_enabled:
        return
    if update.chat_member and update.chat_member.old_chat_member.status in ["member", "administrator", "creator"] and update.chat_member.new_chat_member.status == "left":
        user = update.chat_member.from_user
        first_name = user.first_name
        last_name = user.last_name or ""
        goodbye_message = (
            f"Goodbye {first_name} {last_name} 😢, we're sad to see you leave our community. \n"
            "We wish you all the best! 🙏🏾 and We are going to miss you 🥺🥺 \n" 
            "You're always welcome back at KiraFix💡Community! ❤️"
        )
        await context.bot.send_message(chat_id=update.chat_member.chat.id, text=goodbye_message)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("startwelcome", startwelcome))
    application.add_handler(CommandHandler("stopwelcome", stopwelcome))
    application.add_handler(CommandHandler("startbye", startbye))
    application.add_handler(CommandHandler("stopbye", stopbye))

    
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    application.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, goodbye))

    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
