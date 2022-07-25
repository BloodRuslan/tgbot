from locale import strcoll
from sqlite3 import Timestamp
from tkinter import PhotoImage
from xml.dom.minidom import Document
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from PIL import Image, ImageDraw,ImageFont
import time
import random
import os
abspath=os.path.dirname(os.path.realpath(__file__))

dic = {'а':'a','е':'e', 'ё':'e',
        'о':'o'
}


 
 
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (3, 8, 12)
    font = ImageFont.load_default()
    drawing.text(pos, text, fill=black, font=font)
    photo.save(output_image_path)
 
 


def tr(x):
    t = ''
    for i in x:
        t+=dic.get(i.lower(), i.lower()).upper() if i.isupper() else dic.get(i, i)
    return t



#here u need to enter https://my.telegram.org/auth and get api hash and api id, u can get session string using any ssesion string generator bots (for example, @@StarkStringGenBot, u can find it by searching pyrogram session string generator)
User = Client(session_name="", api_hash="", api_id=)

user_from=[]#chanels from
user_to=#chanels to



@User.on_message((filters.text | filters.media) & ~filters.edited)
async def main(client: Client, message: Message):
  
  
    if message.chat.id in user_from:
        print(message)

        time.sleep(random.randint(1,9))
        if (message.text==None):
         
            if message.caption==None:
                
                if message.photo!=None:

                    filepath=await client.download_media(message.photo,file_name=str(message.message_id)+'.png')
                    print(filepath)

                    img = filepath
                    watermark_text(img, abspath+'/downloads/'+'watermarked.png',
                    text='t.me/TodayTechnoNews',
                    pos=(0, 0))

                    await client.send_photo(chat_id=user_to, photo=abspath+'/downloads/'+'watermarked.png',caption='Живите дружно, ребята')
                    os.remove(abspath+'/downloads/'+str(message.message_id)+'.png')
                    os.remove(abspath+'/downloads/'+'watermarked.png')
                    print(str(message.message_id)+'.png'+"удалён")

                if message.video!=None:
                    print("asdasd")
                    filepath=await client.download_media(message.video,file_name=str(message.message_id)+".mp4")
                    print(filepath)
                    await client.send_video(chat_id=user_to, video=abspath+'/downloads/'+str(message.message_id)+".mp4",caption='Живите дружно, ребята')
                    os.remove(abspath+'/downloads/'+str(message.message_id)+'.mp4')
                    print(str(message.message_id)+'.png'+"удалён")

            elif message.photo!=None:

                filepath=await client.download_media(message.photo,file_name=str(message.message_id)+'.png')
                print(filepath)

                TextEdit=tr(str(message.caption))

                img = filepath
                watermark_text(img, abspath+'/downloads/'+'watermarked.png',
                text='t.me/TodayTechnoNews',
                pos=(0, 0))

                await client.send_photo(chat_id=user_to, photo=abspath+'/downloads/'+'watermarked.png',caption=TextEdit)
                os.remove(abspath+'/downloads/'+str(message.message_id)+'.png')
                os.remove(abspath+'/downloads/'+'watermarked.png')
                print(str(message.message_id)+'.png'+"удалён")

            elif message.video!=None:
                filepath=await client.download_media(message.video,file_name=str(message.message_id)+".mp4")
                print(filepath)

                TextEdit=tr(str(message.caption))
               

                await client.send_video(chat_id=user_to, video=abspath+'/downloads/'+str(message.message_id)+".mp4",caption=TextEdit)
                os.remove(abspath+'/downloads/'+str(message.message_id)+'.mp4')
                print(str(message.message_id)+'.mp4'+"удалён")

         
        elif (message.photo==None) and (message.video==None):
            TextEdit=tr(str(message.text))
            

            await client.send_message(chat_id=user_to, text=TextEdit)


User.run()
