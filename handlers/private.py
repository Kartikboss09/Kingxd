import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        f start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c79c552994c222362d80e.jpg",
        caption=f"""**......⭕𝙎𝙪𝙥𝙥𝙤𝙧𝙩:-  @ROYALUBOT_SUPPORT
       ⭕𝘾𝙍𝙀𝘼𝙏𝙊𝙍:- @ROYALBOY_XD
       ⭕𝘾𝙝𝙖𝙣𝙣𝙚𝙡:- @ROYALYSERBOT
       ⭕𝙊𝙒𝙉𝙀𝙍:- @ROYALBOY_XD
       ⭕𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧:- @KartiK_KinG01
🌟👨‍🎤𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝙏𝙀𝘼𝙈 𝙉𝙊𝙒

 𝙁𝙊𝙍 𝘾𝙃𝘼𝙏𝙏𝙄𝙉𝙂💌 𝙅𝙊𝙄𝙉 - @ved_maitrich007
   𝙄𝙛 𝙔𝙤𝙪 𝙣𝙚𝙚𝙙 𝙖𝙣𝙮 𝙝𝙚𝙡𝙥 𝙩𝙝𝙚𝙣 𝙠𝙞𝙣𝙙𝙡𝙮 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙩𝙤 [👨‍💻𝙇𝙀𝙂𝙀𝙉𝘿👨‍💻](t.me/KartiK_KinG01) ...**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/smoker_robot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/afc66f54a8c2a2002ec3a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐂𝐥𝐢𝐜𝐤 ☑️  𝐑𝐞𝐩𝐨 🌍 💞", url=f"https://github.com/EsportMusicX/SmokerMusicX")
                ]
            ]
        ),
    )
