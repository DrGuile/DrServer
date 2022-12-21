import discord
from discord.ext import commands
import sqlite3


class Economy(commands.Cog):
    def _init_(self, client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        db=sqlite3.connect("DrEcon.sqlite")
        cursor=db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS DrServer (
            user_id INTERGER, wallet INTERGER, bank INTERGER
        )''')
        print("Rejoice lowly humans, The Banker is here")

    @commands.Cog.listener()
    async def on_message(self, dr):
        if dr.author.bot:
            return
        
        author=dr.author
        db=sqlite.connect("DrEcon.sqlite")
        cursor=db.cursor()
        cursor.execute(f"SELECT user_id DrEcon WHERE user_id = {author.id}")
        result-cursor.fetchone()
        if result is None:
            sql=("INSERT INTO DrEcon(user_id, wallet, bank) VALUES (?, ?, ?)")
            val=(author.id, 100, 0)
            cursor.execute(sql, val)

        db.commit()
        cursor.close()
        db.close()

    #commands
    @commands.command()
    async def ping(self, dr):
        latency=str(self.client.latency * 1000)
        await dr.send(f"Pong ",latency,"ms")