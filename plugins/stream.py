from typing import Any
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from urllib.parse import quote_plus
from pyrogram.errors import FloodWait
import asyncio
from info import FILE_TO_LINK_APPURL, FILE_TO_LINK_LOG



STREAM_GEN = bool(FILE_TO_LINK_APPURL and FILE_TO_LINK_LOG)

# streaming feature
async def direct_gen_handler(m: Message):
    if not STREAM_GEN:
        return None, None
    try:
        log_msg = await m.copy(chat_id=FILE_TO_LINK_LOG)
        stream_link, download_link = await gen_link(log_msg)
        if stream_link and download_link:
            markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👀", url=stream_link),
                        InlineKeyboardButton("ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 🗂️", url=download_link),
                    ]
                ]
            )
            return markup

    except FloodWait as e:
        await asyncio.sleep(e.value)
        await direct_gen_handler(m)

def get_media_from_message(m: "Message"):
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(m, attr, None)
        if media:
            return media

def get_hash(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_unique_id", "")[:6]       


async def gen_link(log_msg):
    stream_link = f"{FILE_TO_LINK_APPURL}/watch/{log_msg.id}/?hash={get_hash(log_msg)}"
    download_link = f"{FILE_TO_LINK_APPURL}/{log_msg.id}/?hash={get_hash(log_msg)}"
    return stream_link, download_link
