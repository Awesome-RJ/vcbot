from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>A M A A A O Y G F.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "MusicHelper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I J H A Y RQ")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>@Awesome_Cutiepii A I Y C</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n U {user.first_name} C' J Y G D T H J RQ F U! M S U I N B I G."
            "\n\nO M A @Awesome_Cutiepii T Y G A T A</b>",
        )
        return
    await message.reply_text(
            "<b>@Awesome_Cutiepii U J Y C</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            "<b>U\x1a\x1a\x1a C\x1a\x1a\x1a\x1a\x1a'\x1a L\x1a\x1a\x1a\x1a Y\x1a\x1a\x1a G\x1a\x1a\x1a\x1a! M\x1a\x1a B\x1a F\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a."
        )

        return
