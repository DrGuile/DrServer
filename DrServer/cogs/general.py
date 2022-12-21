import discord
from discord.ext import commands

class General(commands.Cog):
    def _init_(self, client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Rejoice lowly humans, cause I have come")

    #commands
    @commands.command()
    async def ping(self, dr):
        latency=str(self.client.latency * 1000)
        await dr.send(f"Pong ",latency,"ms")

async def setup(client):
    await client.add_cog(General(client))