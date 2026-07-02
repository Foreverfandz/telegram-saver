import asyncio
from telethon import TelegramClient

api_id = 35685408
api_hash = '4e914910845fc9813c1db3656ef444da'

async def main():
    client = TelegramClient('new_clean_session', api_id, api_hash)
    await client.connect()
    print("SENDING_CODE_NOW")
    # Kodni sizning raqamingizga majburiy jo'natadi
    await client.send_code_request('+998998232551')
    print("CODE_SENT_SUCCESSFULLY")

asyncio.run(main())
