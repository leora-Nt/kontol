from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
    await query.answer("Bot Started")
    await query.edit_message_text(
              f"""✨ **Hello** {message.from_user.mention()}\n
💭 I am a selected Telegram Bot that can play high quality music in your group voice chat.**\n
ℹ️ **Information for bot commands click » commands**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔍 Commands", callback_data="menuhelp_cb"),
                    InlineKeyboardButton("👤 Bot Owner", url=f"https://t.me/{OWNER_USERNAME}"),
                ],[
                    InlineKeyboardButton("📨 Group", url=f"https://t.me/full_masti_clubs"),
                    InlineKeyboardButton("📨 Channel", url=f"https://t.me/heartbrokenperson1")
                ],[
                    InlineKeyboardButton("✚ Add Me To Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("menuhelp_cb"))
async def cbcmd(_, query: CallbackQuery):
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
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Admin :-

» /skip - Skip the Song
» /end - Stop Playing Music
» /pause - Pause the track
» /resume - Resumes the Track
» /mute - Mute the Assistant

🌀 Powered By : @tdrki_1**""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("playhelp_cb"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Play :-

» /play - (song name) 
» /play - (song url) 
» /play - (Reply Audio) 
» /search - (song name)

🌀 Powered By : @tdrki_1**""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("extrahelp_cb"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Extra Commands :-

» /ping - Shows the Ping Status
» /start - Starts the Bot
» /id - Get the ID
» /repo - Get the source code 
» /rmd - Clean all the downloads
» /clean - Clean the Storage
» /gcast - broadcast your message 

🌀 Powered By : @tdrki_1**""",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )