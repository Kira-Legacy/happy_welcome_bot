from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

BOT_TOKEN = '8115415891:AAHhC8k4L4aX8uO8z6Qp18jdvElgm_5aty0'

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if update.message and update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            
            if new_member.id == context.bot.id:
                continue
            
            first_name = new_member.first_name
            last_name = new_member.last_name
            welcome_message = (
                f"Hello {first_name }{last_name} 👋🏾, welcome to our awesome community which you are a part of now!  👨🏾‍💻👩🏾‍💻🚀 "
                "We're happy to have you here! Since we are on the same team, feel free to introduce yourself, join the conversation and grow with us. 📈😊"
                "We believe your presence will be a blessing to the community. 🙏🏾"
            )
            await update.message.chat.send_message(welcome_message)


async def start(update, context):
    await update.message.reply_text("Hello! I'm your group's happy welcome bot. I'll greet new members when they join!")

def main():
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
