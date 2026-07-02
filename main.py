import asyncio
from telethon import TelegramClient

# Muqobil mijozlarning bloklanmaydigan universal kalitlari
api_id = 2040
api_hash = 'b1d16e15441413a476da333ec55705f1'

async def main():
    # Eski xatolik qaytarilmasligi uchun sessiya nomini o'zgartiramiz
    client = TelegramClient('clean_final_session', api_id, api_hash)
    await client.connect()
    print("SENDING_CODE_NOW")
    # Raqamingizni aniq xalqaro formatda kiritamiz
    await client.send_code_request('+998882325511')
    print("CODE_SENT_SUCCESSFULLY")

asyncio.run(main())

