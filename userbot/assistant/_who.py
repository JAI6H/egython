# Egython - Userbot
# Whois for Egython - Userbot
# edit ~ <@JAI6H>
# from ~ <ULTRA-X>

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
import os


@asst_cmd("ايدي")
@owner
async def who(event):
    replied_user = await get_user(event)
    try:
        caption = await detail(replied_user, event)
    except AttributeError:
        event.edit("`Could not fetch info of that user.`")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    await event.reply(caption, parse_mode="html")


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await asst(GetFullUserRequest(previous_message.sender_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.get_sender()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await asst(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await asst.get_entity(user)
            replied_user = await asst(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.reply("I don't seem to have interacted with this user before - please forward a message from them to give me control! (like a voodoo doll, I need a piece of them to be able to execute certain commands...)")
            return None

    return replied_user

async def detail(replied_user, event):
 try:
    pro = await bot.get_me()
    boy = pro.id
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    username = replied_user.user.username
    first_name = (
        first_name.replace("\u2060", "")
    )
    last_name = (
        last_name.replace("\u2060", "") if last_name else None
    )
    username = "@{}".format(username) if username else None

    caption = "<b>╔═══*.·:·.☽✧ User Info: ✧☾.·:·.*═══╗</b> \n"
    caption += f"<b>➥ ID:</b> <code>{user_id}</code> \n"
    caption += f"<b>➥ First Name:</b> <code>{first_name}</code> \n"
    if last_name:
      caption += f"<b>➥ Last Name:</b> <code>{last_name}</code> \n"
    if username:
      caption += f"<b>➥ Username:</b> <i>{username}</i> \n"
    caption += f'<b>➥ User link:</b> <i><a href="tg://user?id={user_id}">Perma Link</a></i>'
    if user_id in kimo:
        caption += "\n<b>╚⊶⊶⊶⊶⊶ This is my DEV ;) ⊷⊷⊷⊷⊷╝</b>"
    if not event.sender_id == boy:
       if user_id == boy:
        caption += "\n<b>╚⊶⊶⊶⊶⊶ This is My Master Beware! ⊷⊷⊷⊷⊷╝</b>"
    elif event.sender_id == boy and user_id == boy:
        caption += "\n<b>Hello Master ☺️</b>"
    return caption
 except Exception:
        print("lel")
