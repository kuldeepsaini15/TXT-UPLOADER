from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from helper import get_drm_keys
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
import sys
import os
import random
import re
import tempfile
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import datetime
import aiohttp

bot = Client("bot",
             bot_token= "7836714507:AAE0uMDhthtcFEPoO96xxUxXmeyW6Obz5tU", 
             #bot_token= os.environ.get("BOT_TOKEN"),
             api_id= 23031620,
             api_hash= "31cb00c1cbe580394778b43105864bca")

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/EX_DOLPHIN",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://t.me/EX_DOLPHIN",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Updates Channel",
                url="https://t.me/EX_DOLPHIN",
            ),
            
        ],
    ]
)



Busy = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/EX_DOLPHIN",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://t.me/EX_DOLPHIN",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Join to Check My Status ",
                url="https://t.me/EX_DOLPHIN",
            ),
            
        ],
    ]
)


# List of image URLs
image_urls = [
    "https://graph.org/file/9dbe3901f43b11e98e6f0.jpg",
    "https://graph.org/file/c5ec0a02be408b354d3fc.jpg",
    "https://graph.org/file/c186818a566c501f14abf.jpg",
    "https://graph.org/file/850ef256ede1370257b5d.jpg",
    "https://graph.org/file/40700542e58889b5c42fe.jpg",
    "https://graph.org/file/94a7875bb51006e7bd528.jpg",
    # Add more image URLs as needed
]



@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    # Choose a random image URL from the list
    random_image_url = random.choice(image_urls)
    
    
    # Caption for the image
    caption = f"**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫  👋!\n\n➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ♥️\n➠ Can Extract Videos & Pdf Form Your Text File and Upload to Telegram\n\n➠ 𝐔𝐬𝐞 /drm 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞  \n\n➠𝐌𝐚𝐝𝐞 𝐁𝐲: @EX_DOLPHIN **\n"
    
    # Send the image with the caption
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        reply_markup=keyboard
    )

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["txt"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('𝕤ᴇɴᴅ ᴛxᴛ ғɪʟᴇ ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n144,240,360,480,720,1080 please choose quality")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg » https://graph.org/file/ce1723991756e48c35aa1.jpg \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif "tencdn.classplusapp" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "media-cdn.classplusapp" in url:
            	url = f"https://drm-api-six.vercel.app/api/cp/dl?url={url}"
            	
            elif "cwmediabkt99.crwilladmin.com" in url:
            	url = url.replace(' ', '%20')
            elif ".pdf*abcdefg" in url:
             a = url.replace('*abcdefg', '')
             url = a
            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            referer = "https://www.youtube.com"

            if "jw-prod" in url:
                cmd = f'yt-dlp --cookies "{cookies_path}" --user-agent "{user_agent}" --referer "{referer}" -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp --cookies "{cookies_path}" --user-agent "{user_agent}" --referer "{referer}" -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[▶️] Vid_ID :** {str(count).zfill(3)}\n\n**Video Title :** {name1}\n\n**Batch Name :** {raw_text0}\n\n**Extracted By ➤ {MR}**'
                cc1 = f'**[📑] Pdf_ID :** {str(count).zfill(3)}\n\n**File Title :** {name1}\n\n**Batch Name :** {raw_text0}\n\n**Extracted By ➤ {MR}**'                
                if "*" in url:
                     a, k = url.split("*", 1)
                     url = a
                     key = k
                     try:
                      	if ".pdf" in a:
                      		Show = f"⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »\n\n📝Name » {name}\n❄Quality » {raw_text2}\n\n🔗URL » {url}"
                      		prog = await m.reply_text(Show)
                      		file_path = await helper.download_file(url, name)
                      		copy = helper.decrypt_file(file_path, key)
                      		filename = file_path
                      		await prog.delete(True)
                          await bot.send_document(chat_id=-1002360995423, document=filename, caption=cc1)
                      		count += 1
                      	else:
                      		Show = f"⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »\n\n📝Name » {name}\n❄Quality » {raw_text2}\n\n🔗URL » {url}"
                      		prog = await m.reply_text(Show)
                      		file_path = await helper.download_file(url, name)
                      		copy = helper.decrypt_file(file_path, key)
                      		filename = file_path
                      		await prog.delete(True)
                      		await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                      		count += 1
                     except FloodWait as e:
                      await m.reply_text(str(e))
                      time.sleep(1)
                      continue
                
                elif "drive" in url or ".ws" in url or "cwmediabkt99.crwilladmin.com" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(2)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


bot.run()
