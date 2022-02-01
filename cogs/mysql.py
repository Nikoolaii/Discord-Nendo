import discord
from discord.ext import commands
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

prefixint = "n!"

class Mysql(commands.Cog):

    def __init__(self, client):
        self.client = client 

    try:

        load_dotenv()
        db_host = os.getenv("DB_HOST")
        db_db = os.getenv("DB_DB")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")


        connection = mysql.connector.connect(host=db_host,
                                            database=db_db,
                                            user=db_user,
                                            password=db_password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    @commands.command(pass_context = True)
    async def sendmsg(self,ctx):
        load_dotenv()
        db_host = os.getenv("DB_HOST")
        db_db = os.getenv("DB_DB")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        connection = mysql.connector.connect(host=db_host,
                                    database=db_db,
                                    user=db_user,
                                    password=db_password)
        
        cursor = connection.cursor()
        query = ("SELECT msg FROM phrases WHERE servid = %s")
        srvid = ctx.message.guild.id
        cursor.execute(query,(srvid,))
        #record = cursor.fetchone()
        for(msg) in cursor:
            await ctx.send(msg)

def setup(client):
    client.add_cog(Mysql(client))