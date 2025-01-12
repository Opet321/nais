# Copyright (C) 2020 - Dragon Userbot

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory 
from pyrogram.raw import functions
from asyncio import sleep
from feedback.base.db_client import db, pmstatus, contacts, supports




@Client.on_message(
    filters.private
    & ~filters.me
    & ~filters.bot
    & ~contacts
    & ~supports
    & pmstatus
)
async def _antipm_(client: Client, message: Message):
    userpm = await client.resolve_peer(message.chat.id)
    if db.get("core.antipm", "pmreport", False):
        await client.invoke(
            functions.messages.ReportSpam(
                peer=userpm
            )
        )
    if antipmdb.get("core.antipm", "pmblock", False):
        await client.invoke(
            functions.contacts.Block(
                id=userpm
            )
        )
    msg = await client.send_message(
        message.chat.id,
        "Sorry... No-PMs!"
    )
    for countdown in ["3", "2", "1"]:
        await sleep(1)
        await msg.edit(countdown)
    await client.invoke(
        functions.messages.DeleteHistory(
            peer=userpm,
            max_id=0,
            revoke=True
        )
    )


@Client.on_message(filters.command("antipm") & filters.me)
async def _antipm(_, message: Message):
    if len(message.command) == 1:
        if db.get("core.antipm", "status", False):
            await message.edit(
                "Anti-PM Status: ON!\n"
                f"Deactivated: <code>{prefix}antipm off</code>"
            )
        else:
            await message.edit(
                "Anti-PM Status: OFF!\n"
                f"Activated: <code>{prefix}antipm on</code>"
            )
    elif message.command[1] == "on":
        db.set("core.antipm", "status", True)
        await message.edit("Anti-PM ON!")
    elif message.command[1] == "off":
        db.set("core.antipm", "status", False)
        await message.edit("Anti-PM OFF!")
    else:
        await message.edit(
            "Usage: "
            f"<code>{prefix}antipm </code>"
            "[on|off]"
        )