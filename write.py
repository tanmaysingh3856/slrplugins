
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from userbot import catub
from ..helpers.utils import reply_id
from . import *
from ..helpers.utils import edit_delete
plugin_category = "extra"
    
@catub.cat_cmd(
    pattern="write(?:\s|$)([\s\S]*)",
    command=("write", plugin_category),
    info={
        "header": "To write given text on paper.",
        "usage": "{tr}write <message/reply>",
        "examples": "{tr}write Hello World",
    },
)

async def writer(e):
        "Write-er"
        reply_to_id = await reply_id(e)
        text = e.pattern_match.group(1)
        if not text:
            return await edit_delete(e, "`Give me some text`", 6)
        k = await e.edit("`Processing ...`")
        fontdl = os.system("cd temp && wget https://index.ivuxy.workers.dev/0:/Document/assfont.ttf")
        temdl = os.system("cd temp && wget https://index.ivuxy.workers.dev/0:/Photo/template.jpg")
        img = Image.open("temp/template.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("temp/assfont.ttf", 30)
        x, y = 150, 140
        wrapit = textwrap.wrap(text, width=55)
        words = "\n".join(wrapit)
        lines = (text)
        line_height = font.getsize("hg")[1]
        draw.text((x, y), words, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
        file = "pic.jpg"
        img.save(file)
        await e.client.send_file(e.chat_id, file, reply_to=reply_to_id)
        await e.delete()
        os.remove(file)
        os.remove("temp/template.jpg")
        os.remove("temp/assfont.ttf")
