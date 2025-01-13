# Copyright (C) 2020 - Dragon Userbot

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory 
from pyrogram.raw import functions 
from pyrogram.types import InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent, InlineQuery, Message
from asyncio import sleep
from feedback.base.db_client import db, pmstatus, contacts, supports


cmd = "."

async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def is_antipm_(f, client, message):
    user_id = client.me.id
    antipm_c = await check_antipm(user_id)
    if antipm_c:
        return bool(True)
    else:
        return bool(False)

is_antipm = filters.create(func=is_antipm_, name="is_antipm_")

@Client.on_message(filters.command(["autopurge"], cmd) & filters.me)
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
   ~filters.me & ~filters.bot & filters
     .private & is_antipm 
)
async def handle_antipm(client: Client,
  message: Message) -> None: 
    if message.from_user.is_contact is True:
        return 
    if message.from_user.is_support is True:
        return 
    if message.from_user.id == OWNER: 
        return
      
    results = await client.get_inline_bot_results("@eyecosbot",  query="pmpermit") 
    await client.send_inline_bot_result(message.chat.id, results.query_id, results.results[0].id)
    peer_id = await client.resolve_peer(message.chat.id)  
    await sleep (8)
    await client.invoke(DeleteHistory(peer=peer_id, max_id=0, revoke=True))




@Client.on_inline_query() 
async def handle_inline(client: Client, inline: InlineQuery) -> None: 
    inline_query = inline.query 
    if inline_query.strip().lower().split()[0] == "pmpermit": 
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="contact me", user_id=client.me.id)]] 
        ) 
        await inline.answer( 
            results=[InlineQueryResultArticle(
                id=str(uuid4()), 
                title="Pmpermit",
                input_message_content 
                  =InputTextMessageContent("<b><blockquote>Maaf saya tidak bisa menerima PM, Silahkan hubungi saya melalui bot, klik tombol di bawah ini</b></blockquote>"), 
                reply_markup=keyboard 
            )]
        )

