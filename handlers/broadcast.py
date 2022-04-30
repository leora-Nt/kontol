# Copyright (C) 2022 By KATIL
# Originally written by levina on github
# Broadcast function


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as aditya

SUDO_USERS = "1963422158"

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Starting broadcast ...`")
        if not message.reply_to_message:
            await wtf.edit("**__Please reply to message to start Broadcast...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Broadcasting` \n\n**Sent To:** `{sent}` Chats \n**Failed In:** {failed} Chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`Gcast succesfully` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
