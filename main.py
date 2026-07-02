import os
import asyncio
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from telethon import TelegramClient

# Render o'chib qolmasligi uchun soxta port
def run_dummy_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

api_id = 35685408
api_hash = '4e914910845fc9813c1db3656ef444da'

client = TelegramClient('new_clean_session', api_id, api_hash)

SOURCE_CHAT = -1002565645630  # Manba private kanal
TARGET_CHAT = 'kanehsii'      # Sizning kanalingiz
SPECIFIC_MSG_ID = 15          # Aynan siz bergan 15-xabar

async def main():
    await client.start()
    print(f"Userbot aynan {SPECIFIC_MSG_ID}-xabarni ko'chirishni boshladi...")
    
    try:
        # Faqatgina shu ID dagi bitta xabarni olamiz
        message = await client.get_messages(SOURCE_CHAT, ids=SPECIFIC_MSG_ID)
        
        if message and message.media:
            print(f"Video topildi (ID: {message.id}). Yuklanmoqda...")
            temp_path = f"temp_{message.id}.mp4"
            
            await client.download_media(message, file=temp_path)
            print("Kanalingizga yuborilmoqda...")
            await client.send_file(TARGET_CHAT, temp_path, caption=message.text or "")
            
            if os.path.exists(temp_path):
                os.remove(temp_path)
            print("Muvaffaqiyatli yuklab bo'lindi!")
        else:
            print("Bu ID ostida media fayl topilmadi yoki xabar o'chirilgan!")
            
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

with client:
    client.loop.run_until_complete(main())
    
    
