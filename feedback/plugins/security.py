# Copyright (C) 2020 - Dragon Userbot

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory 
from pyrogram.raw import functions
from asyncio import sleep


async def is_antipm_(f, client, message):
    user_id = client.me.id
    antipm_c = await check_antipm(user_id)
    if antipm_c:
        return bool(True)
    else:
        return bool(False)

is_antipm = filters.create(func=is_antipm_, name="is_antipm_")

@Client.on_message(filters.command(["autopurge"] & filters.me)
async def set_antipm(client, message):
    try:
        if len(message.command) < 2:
            await message.reply("Please specify 'on' or 'off'.", quote=True)
            return
        
        if message.command[1] == "on":
            user_id = client.me.id
            await go_antipm(user_id)
            await message.reply("<b>Anti-PM activated!!</b>", quote=True)
        elif message.command[1] == "off":
            user_id = client.me.id
            await no_antipmk(user_id)
            await message.reply("<b>Anti-PM deactivated!!</b>", quote=True)
        else:
            kontols = await check_antipm(client.me.id)
            kurukuru = kontols.get("antipm", "False")
            await message.reply(f"<b>Anti-PM status:</b> <code>{kurukuru}</code>\n<b>To Activate use</b> <code>antipm on/off</code>", quote=True)
    except Exception as e:
        print(f"Error in set_antipm: {e}")
        kontols = await check_antipm(client.me.id)
        kurukuru = kontols.get("antipm", "False")
        await message.reply(f"<b>Anti-PM status:</b> <code>{kurukuru}</code>\n<b>To Activate use</b> <code>antipm on/off</code>", quote=True)


@Client.on_message(
    ~filters.me
    & ~filters.bot
    & filters.private
    & is_antipm
)
async def antipm_er(client, message):
    anuku = await client.resolve_peer(message.chat.id)
    if message.from_user.is_contact is True:
        return
    if message.from_user.is_support is True:
        return
    if message.from_user.id == OWNER:
        return 
    await client.invoke(DeleteHistory(peer=anuku, max_id=0, revoke=True))