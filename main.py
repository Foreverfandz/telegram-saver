import os
import asyncio
from telethon import TelegramClient

api_id = 35685408
api_hash = '4e914910845fc9813c1db3656ef44475'
source_channel = -1002565645630
target_channel = 'kanehsii'

client = TelegramClient('new_clean_session', api_id, api_hash)

async def main():
    print("Server connected successfully. Scanning channel...")
    async for message in client.iter_messages(source_channel, reverse=True):
        if message.video:
            temp_path = f"temp_{message.id}.mp4"
            print(f"Downloading video ID: {message.id} on cloud server...")
            try:
                await client.download_media(message.video, file=temp_path)
                print(f"Uploading video ID: {message.id} to @{target_channel}...")
                await client.send_file(target_channel, temp_path, caption=message.text)
                print(f"Status: Success for ID {message.id}")
            except Exception as e:
                print(f"Status: Error for ID {message.id} -> {e}")
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            await asyncio.sleep(4)

with client:
    client.loop.run_until_complete(main())
