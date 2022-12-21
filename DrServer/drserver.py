import asyncio
import discord
import os
from discord.ext import commands
import logging

intents = discord.Intents.all()
intents.members = True
intents.message_content=True
client=commands.Bot(command_prefix="dr ", intents=intents)

async def load():
    for filename in os.path("C:/Users/ACER/Desktop/Preet/General/Discord_Bots/DrServer/cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def unload():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.unload_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await client.start("MTA0NjM1NzYyODM0NDg2MDY3Mg.GdAYYG.58_ZpbxRujw1Mdr0Wh8mtRfmlWWVMaxpD9DVJ0")

@commands.command()
async def ping(self, dr):
    await dr.send(f'Pong! {round(client.latency * 1000)}ms')

logging.basicConfig(level=logging.INFO)
asyncio.run(main())