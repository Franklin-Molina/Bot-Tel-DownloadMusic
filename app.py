from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import MessageEntity
import tempfile as tf
import os
import urllib.request

import settings




endpoint_link = "https://ipa-bot-telem.herokuapp.com/song/?query="


import urllib.request, json

def fetchjson(url):
    resp= urllib.request.urlopen(url)   #Concatenar las url
    return json.loads(resp.read().decode())

def start(update, context):
    #context.bot.sendMessage(chat_id= update.effective_chat.id,     
    text= "Hola: {yourname}  !"  .format(yourname=update.effective_user.full_name) + "\n \n" "Este es un bot 🤖 para descargar musica ✅🎶" + "\n\n" + "Authors: 🥷🏻 Franklin Molina & Carlos Paz 🥷🏻"
   
  
    update.message.reply_text(text)

def download(update, context):
    
    x = update.message.parse_entities(types = MessageEntity.URL)
  
    msg = update.message.reply_text("Estamos trabaando...")
    for i in x:            
        try:
            rjson = fetchjson(endpoint_link + x[i])
            #print("resultado:",rjson)
            title = rjson["album"]
            link = rjson["media_url"]
            update.message.reply_document(link, caption = "Title:  {}.".format(title))
            msg.delete()
            return            
        except:
            #raise
            continue
        if "error" in rjson:
            continue
        
                               
    msg.edit_text("No se encontro la url, intente otravez")


updater = Updater(token=settings.TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.entity(MessageEntity.URL),download))

updater.start_polling()
updater.idle()
