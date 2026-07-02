import asyncio
from telethon import TelegramClient

# Telegram'ning eng oxirgi va ishchi rasmiy kalitlari
api_id = 21743126
api_hash = '8280f5bc91b61c94d0b13cf48834c772'

async def main():
    client = TelegramClient('new_clean_session', api_id, api_hash)
    await client.connect()
    print("SENDING_CODE_NOW")
    # Kodni sizning raqamingizga jo'natish buyrug'i
    await client.send_code_request('+998998232551')
    print("CODE_SENT_SUCCESSFULLY")

asyncio.run(main())

