from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
    await query.edit_message_text(
              f"""โจ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})\n
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

@Client.on_callback_query(filters.regex("menuhelp_cb"))
async def mhcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**This is the help menu for using this bot.

All commands can be used using** /.""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Play", callback_data="playhelp_cb"),
                ],[
                    InlineKeyboardButton("Admin", callback_data="adminhelp_cb"),
                    InlineKeyboardButton("Extra", callback_data="extrahelp_cb"),
                ],[
                    InlineKeyboardButton("Back", callback_data="cb_start"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("adminhelp_cb"))
async def ahcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Admin :-

ยป /skip - Skip the Song
ยป /end - Stop Playing Music
ยป /pause - Pause the track
ยป /resume - Resumes the Track
ยป /mute - Mute the Assistant

๐ Powered By : @tdrki_1**""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("playhelp_cb"))
async def phcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Play :-

ยป /play - (song name) 
ยป /play - (song url) 
ยป /play - (Reply Audio) 
ยป /search - (song name)

๐ Powered By : @tdrki_1**""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("extrahelp_cb"))
async def ehcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Extra Commands :-

ยป /ping - Shows the Ping Status
ยป /start - Starts the Bot
ยป /id - Get the ID
ยป /repo - Get the source code 
ยป /rmd - Clean all the downloads
ยป /clean - Clean the Storage
ยป /gcast - broadcast your message 

๐ Powered By : @tdrki_1**""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )
