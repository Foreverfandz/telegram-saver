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

SOURCE_CHAT = -1002565645630
TARGET_CHAT = '@kanehsii'  # Kanalni topish oson bo'lishi uchun @ belgisini qo'shdik
SPECIFIC_MSG_ID = 15

async def main():
    await client.start()
    print("Userbot ishga tushdi...")
    
    # Birinchi navbatda serverda tayyor turgan faylni tekshiramiz
    local_file = f"temp_{SPECIFIC_MSG_ID}.mp4"
    
    try:
        if os.path.exists(local_file):
            print(f"Serverda tayyor fayl topildi: {local_file}. Kanalingizga yuborishga urinib ko'ramiz...")
            await client.send_file(TARGET_CHAT, local_file, caption="15-Darslik")
            print("Video kanalingizga muvaffaqiyatli yuborildi!")
            os.remove(local_file)
            return
            
        # Agar fayl serverda yo'q bo'lsa, qaytadan yuklab oladi
        message = await client.get_messages(SOURCE_CHAT, ids=SPECIFIC_MSG_ID)
        if message and message.media:
            print(f"Video manbadan topildi (ID: {message.id}). Yuklanmoqda...")
            await client.download_media(message, file=local_file)
            print("Kanalingizga yuborilmoqda...")
            await client.send_file(TARGET_CHAT, local_file, caption=message.text or "")
            if os.path.exists(local_file):
                os.remove(local_file)
            print("Muvaffaqiyatli bajarildi!")
        else:
            print("Bu ID ostida media topilmadi!")
            
    except Exception as e:
        print(f"Jarayonda xatolik bo'ldi: {e}")
        print("Iltimos, botingiz maqsadli kanalda admin ekanligini tekshiring!")

with client:
    client.loop.run_until_complete(main())
    
