import logging
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

# بدء التعامل مع المستخدمين الجدد
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("مرحباً! هذا بوت متجر طلبات شعبية.
اكتب /register للتسجيل.")

# تسجيل المستخدم
async def register(update: Update, context: CallbackContext):
    await update.message.reply_text("تم استلام طلب التسجيل. سيتم تأكيده من قبل الإدارة.")

# إعداد التطبيق
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))

    app.run_polling()

if __name__ == "__main__":
    main()