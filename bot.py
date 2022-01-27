from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5163195332:AAFe3nV2dcaVIGjH7MyXRjldpeg5OEf7bnc',use_context = True )

def start(update,context):
  user = update.message.from_user
 update.message.reply_html('👋🏻Assalomu alaykum <b>{}!</b>\n \n<b> Ushbu bot orqali\n matnlarni eng-uzb shaklida\n tarjima qila olasiz.\n Botga matn yuboring</b>'.
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
