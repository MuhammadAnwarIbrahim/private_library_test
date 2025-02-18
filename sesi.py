import asyncio
import os
from pyrogram import Client


# Get from my.telegram.org
api_id = 26749580 
# Get from my.telegram.org
api_hash = "1c5d89ec714bc2134bb902c4acf12fdf"
# Get a bot from botfather
TG_BOT_TOKEN="7712910920:AAFF7RdvPbvNgDPpvbtD7q5sFlU9sAU5qgo"

# Authorized users to use this bot
auth_users = ["5503333018", "718497847"]
# Nama session yang akan disimpan
tg_user_session_name = "my_account"
session_file = f"{tg_user_session_name}.session"

async def create_and_export_session():
    app = Client(tg_user_session_name, api_id=api_id, api_hash=api_hash)

    print("Jalankan aplikasi dan masukkan kredensial jika diminta...")
    await app.start()

    # Mengekspor session string
    session_string = await app.export_session_string()
    with open("session_string.txt", "w") as file:
        file.write(session_string)

    print("Session telah berhasil di rekam silakan gunakan pyhton main.py.")

    await app.stop()

    # Hapus file session setelah berhasil mengekspor session string
    if os.path.exists(session_file):
        os.remove(session_file)
        print(f"File '{session_file}' telah dihapus.")
    else:
        print(f"File '{session_file}' tidak ditemukan.")


def run_bot():
    from bot import Bot
    Bot().run()

if __name__ == "__main__":
    
    if os.path.exists(session_file):
        run_bot()
    else:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(create_and_export_session())
        # from bot import Bot
        run_bot()



