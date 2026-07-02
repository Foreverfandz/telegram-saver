import os
import asyncio
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from telethon import TelegramClient

# 1. RENDER UCHUN SOXTA PORT OCHISH (O'chib qolmasligi uchun)
def run_dummy_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# 2. TELEGRAM USERBOT KODI
api_id = 35685408
api_hash = '4e914910845fc9813c1db3656ef444da'

client = TelegramClient('new_clean_session', api_id, api_hash)

# Kanallar va boshlanish xabari
SOURCE_CHAT = -1002565645630  # Manba private kanal
START_MESSAGE_ID = 14         # Siz aytgan 14-xabardan boshlash
TARGET_CHAT = 'kanehsii'      # Sizning kanalingiz

async def main():
    await client.start()
    print("Userbot muvaffaqiyatli ishga tushdi...")
    
    # 14-xabardan boshlab oldinga qarab barcha darsliklarni yuklash
    async for message in client.iter_messages(SOURCE_CHAT, min_id=START_MESSAGE_ID - 1, reverse=True):
        if message.video:  # Faqat videolarni saralab olish
            try:
                print(f"Yuklanmoqda: Video ID {message.id}")
                # Faylni yuklab olib, maqsadli kanalga yuborish
                temp_path = f"temp_{message.id}.mp4"
                await client.download_media(message, file=temp_path)
                
                print(f"Kanala yuklanmoqda: Video ID {message.id}")
                await client.send_file(TARGET_CHAT, temp_path, caption=message.text or "")
                
                # Vaqtinchalik faylni o'chirish
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
                await asyncio.sleep(5)  # Telegram bloklab qo'ymasligi uchun cheklov
            except Exception as e:
                print(f"Xatolik yuz berdi (ID {message.id}): {e}")
                await asyncio.sleep(10)

    print("Hamma darsliklar ko'chirib bo'lindi!")

with client:
    client.loop.run_until_complete(main())
    
