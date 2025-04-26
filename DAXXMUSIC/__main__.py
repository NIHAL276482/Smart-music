import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DAXXMUSIC import LOGGER, app, userbot
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.misc import sudo
from DAXXMUSIC.plugins import ALL_MODULES
from DAXXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DAXXMUSIC.plugins" + all_module)
    LOGGER("DAXXMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("DAXXMUSIC").error(
            "𝐏𝐋𝐙 𝐒𝐓𝐀𝐑𝐓 𝐘𝐎𝐔𝐑 𝐋𝐎𝐆 𝐆𝐑𝐎𝐔𝐏 𝐕𝐎𝐈𝐂𝐄𝐂𝐇𝐀𝐓\𝐂𝐇𝐀𝐍𝐍𝐄𝐋\n\n神 𝗞ɪʀᴀ 𝐁𝐎𝐓 𝐒𝐓𝐎𝐏........"
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("神 𝗞ɪʀᴀ").info(
        "╔═════☠️ஜ۩💋۩ஜ☠️════╗\n  🍁𝐌𝐀𝐃𝐄 𝐁𝐘 𝐌𝐑 LUFFY🍁\n╚═════☠️ஜ۩💋۩ஜ☠️════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("神 𝗞ɪʀᴀ").info("𝐒𝐓𝐎𝐏 神 𝗞ɪʀᴀ 𝐌𝐔𝐒𝐈𝐂⚡ 𝐁𝐎𝐓..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
