from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
    await query.answer("Bot Started")
    await query.edit_message_text(f"✨ **Hello** {message.from_user.mention()}\n\n💭 I am a selected Telegram Bot that can play high quality music in your group voice chat.**\n\nℹ️ **Information for bot commands click » commands**",
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
    await query.edit_message_text(f"**This is the help menu for using this bot.\n\nAll commands can be used using** /.",
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
        f"""**Admin :-**\n\n» /skip - Skip the Song\n» /end - Stop Playing Music\n» /pause - Pause the track\n» /resume - Resumes the Track\n» /mute - Mute the Assistant",
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
    await query.edit_message_text(f"**Play :-**\n\n» /play - (song name) \n» /play - (song url) \n» /play - (Reply Audio) \n» /search - (song name)",
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
    await query.edit_message_text(f"**Extra Commands :-\n\n» /ping - Shows the Ping Status\n» /start - Starts the Bot\n» /id - Get the ID\n» /repo - Get the source code \n» /rmd - Clean all the downloads\n» /clean - Clean the Storage\n» /gcast - broadcast your message",
           reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("Back", callback_data="menuhelp_cb"),
                ],
            ]
        ),
    )
