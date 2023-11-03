from pyrogram import Client, filters
from pyrogram.types import Message
from utils import Compiler
from re import search

from config import NAME, API_ID, API_HASH, BOT_TOKEN, CPP17, CPP14, CPP11

app = Client(name=NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply("Hello, I'm a bot!", quote=True)

@app.on_message(filters.command("help"))
async def help(_, message: Message):
    await message.reply("Hi, It's GCC Compiler for C/C++.\nIf you want to run specific code, use /run command and read the instructions.", quote=True)

@app.on_message(filters.command("run", prefixes=["/", "!"]))
async def run(_, message: Message):
    compiler = Compiler()

    if len(message.command) < 2:
        return await message.reply("**Error:** Too few arguments! Please specify the code to run.\n\n**Instructions:** To run any code: \n ```sh\n!run [code]```\n\nTo specify another standard except 2017, then add std=standard argument to your command.\n\n**Example:** ```sh\n!run std=14 [code] ```", quote=True)
    if m:=search("std\=(\d+)", message.text):
        code = message.text[m.end():].strip()
        std = m.group(1)
        if std not in (CPP17, CPP14, CPP11):
            return await message.reply("This standart not supported for now!", quote=True)
        elif std == CPP11:
            std = CPP14
        else:
            std = CPP17
        context = compiler.run(code, std)
    else:
        code = message.text.split(maxsplit=1)[1].strip()
        context = compiler.run(code)
        
    return await message.reply(context.formatter(code))

app.run()
