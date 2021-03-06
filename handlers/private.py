import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
     await message.reply_text(f"""โจ **Hello** {message.from_user.mention()}\n
๐ญ I am a selected Telegram Bot that can play high quality music in your group voice chat.**\n
โน๏ธ **Information for bot commands click ยป commands**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ Commands", callback_data="menuhelp_cb"),
                    InlineKeyboardButton("๐ค Bot Owner", url=f"https://t.me/{OWNER_USERNAME}"),
                ],[
                    InlineKeyboardButton("๐จ Group", url=f"https://t.me/full_masti_clubs"),
                    InlineKeyboardButton("๐จ Channel", url=f"https://t.me/heartbrokenperson1")
                ],[
                    InlineKeyboardButton("โ Add Me To Your Group โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("๐ `PONG!!`\n" f"โก๏ธ `{delta_ping * 1000:.3f} ms`")



@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("`Click on the Button given below to Get the Bot Source Code.`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ๏ธ ๐๐จ๐ฎ๐ซ๐๐ ", url=f"https://github.com/bhumiharsaurabh/katilmusicx")
                ]
            ]
        ),
    )
