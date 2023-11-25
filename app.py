#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Discord bot for the Scarlet Pigs server
   Handles the discord bot side of event management and 
   various administrative tasks for the Scarlet Pigs server.
"""
__author__ = "Rasmus Tanggaard (Ridderrasmus)"
__credits__ = ["Rasmus Tanggaard (Ridderrasmus)"]
__maintainer__ = "Rasmus Tanggaard (Ridderrasmus)"


# Handle imports
from restservice import RestClient
from models import *
from cogs import register as cogs
import discord
import os

# Setup global variables
def define_global_vars():
    global BOT_TOKEN
    BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create Discord Client class
class SPiglet(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default() + discord.Intents.members)
        self.synced = False        
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            cogs.register_cogs(self)
            self.synced = True
        print(f'Logged on as {self.user}!')


# Main function
def main():
    # Define global variables
    define_global_vars()
    
    # Create Discord Client
    dClient = SPiglet()    
    
    # Setup other services 
    serv = RestClient('api-link-here')
    
    resp = serv.get("/req")
    
    myEvent = Event.from_dict(resp)
    
    # Start Discord Client
    dClient.run(BOT_TOKEN)

if __name__ == '__main__':
    main()