import os
import asyncio
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from telethon import TelegramClient

# Dummy server to keep Render web service alive
def run_dummy_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# Connection configurations
api_id = 35685408
api_hash = '4e914910845fc9813c1db3656ef444da'

client = TelegramClient('new_clean_session', api_id, api_hash)

# Chat configuration
SOURCE_CHAT = -1002565645630         # Source private channel ID
TARGET_CHAT = 'https://t.me/+aiVkisWq0OljZDc6'  # Your new target chat invite link

# Message range configuration
START_MSG_ID = 159
END_MSG_ID = 179

async def main():
    await client.start()
    print("Userbot started successfully. Preparing to process messages...")
    
    # Loop through the specified range of message IDs
    for msg_id in range(START_MSG_ID, END_MSG_ID + 1):
        print(f"Processing message ID: {msg_id}...")
        try:
            # Fetch specific message from source
            message = await client.get_messages(SOURCE_CHAT, ids=msg_id)
            
            if message and message.media:
                print(f"Media found in message {msg_id}. Downloading file...")
                
                # Download media using its native filename/extension
                downloaded_file = await client.download_media(message)
                
                if downloaded_file and os.path.exists(downloaded_file):
                    print(f"File downloaded: {downloaded_file}. Forwarding to target chat...")
                    
                    # Send to the new target link with original text caption
                    await client.send_file(TARGET_CHAT, downloaded_file, caption=message.text or "")
                    print(f"Message {msg_id} forwarded successfully!")
                    
                    # Clean up file to save space on Render
                    os.remove(downloaded_file)
                else:
                    print(f"Failed to download media for message {msg_id}.")
            elif message:
                print(f"Message {msg_id} has no media. Forwarding text content...")
                await client.send_message(TARGET_CHAT, message.text or "")
                print(f"Text from message {msg_id} forwarded successfully!")
            else:
                print(f"Message {msg_id} not found or has been deleted.")
                
            # Anti-flood sleep interval
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"Error processing message {msg_id}: {e}")
            print("Ensure the userbot account is an authorized member of both chats.")

with client:
    client.loop.run_until_complete(main())
    
