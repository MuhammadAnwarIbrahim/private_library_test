from os.path import exists

from pyrogram import Client, enums

if exists("./config.py"):
    from config import LOGGER, Config
else:
    from sample_config import LOGGER, Config

from user import User

from sesi import tg_user_session_name

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            tg_user_session_name,
            api_hash=Config.API_HASH,
            api_id=Config.APP_ID,
            bot_token=Config.TG_BOT_TOKEN,
            sleep_threshold=0,
            plugins={"root": "plugins"},
        )
        self.LOGGER = LOGGER

    async def start(self, use_qr=False, *args, **kwargs):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"Bot {usr_bot_me.first_name} (@{usr_bot_me.username}) started!"
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
