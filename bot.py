from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5163195332:AAFe3nV2dcaVIGjH7MyXRjldpeg5OEf7bnc',use_context = True )

def start(updater,context):
 update = update.message.from_user
 updater.message.reply_html('👋🏻Assalomu alaykum <b>{}!</b>\n \n<b> Ushbu bot orqali matnlarni\n eng-uzb shaklida tarjima\n qila olasiz. Botga\n matn yuboring</b>.')
 format(user.first_name))
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='uz') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
