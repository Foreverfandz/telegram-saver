import os
import asyncio
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from telethon import TelegramClient

# Render o'chib qolmasligi uchun soxta server
def run_dummy_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

api_id = 35685408
api_hash = '4e914910845fc9813c1db3656ef444da'

client = TelegramClient('new_clean_session', api_id, api_hash)

SOURCE_CHAT = -1002565645630  # Manba private kanal
TARGET_CHAT = '@kanehsii'      # Sizning kanalingiz
SPECIFIC_MSG_ID = 179         # Siz bergan yangi xabar ID-si

async def main():
    await client.start()
    print(f"Userbot {SPECIFIC_MSG_ID}-xabarni tekshirishni boshladi...")
    
    try:
        # Xabarni manba kanaldan olamiz
        message = await client.get_messages(SOURCE_CHAT, ids=SPECIFIC_MSG_ID)
        
        if message and message.media:
            print("Fayl topildi! Yuklanmoqda (nomi va formati avtomatik aniqlanadi)...")
            
            # Faylni o'z formati (PDF, MP4, JPG va h.k.) bilan yuklab olish
            downloaded_file = await client.download_media(message)
            
            if downloaded_file and os.path.exists(downloaded_file):
                print(f"Fayl muvaffaqiyatli yuklandi: {downloaded_file}. Kanalingizga yuborilmoqda...")
                
                # Kanalingizga faylni aslicha yuborish
                await client.send_file(TARGET_CHAT, downloaded_file, caption=message.text or "")
                print("Muvaffaqiyatli yuborildi! 🚀")
                
                # Joy bo'shatish uchun serverdan o'chirish
                os.remove(downloaded_file)
            else:
                print("Faylni yuklab olishda xatolik yuz berdi!")
        else:
            print(f"ID {SPECIFIC_MSG_ID} ostida hech qanday media (fayl/video) topilmadi yoki xabar o'chirilgan!")
            
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        print("Eslatma: Userbot profilingiz ushbu private guruh/kanal ichida a'zo ekanligini qayta tekshiring!")

with client:
    client.loop.run_until_complete(main())
    
