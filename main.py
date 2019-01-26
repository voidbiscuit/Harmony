# Imports
import discord
import datetime

from ui import console
from commands import controller, misc

# Init
client = discord.Client()
TOKEN = open('config/token').read()
command_prefix = open('config/token').read()

console.__bot_message()


@client.event
async def on_message(message):
    if message.author.bot and not message.author == client.user:
        return  # Exit if the message is from another bot
    console.print_message(message)  # Print the message to Python console
    if message.author == client.user:
        return  # Don't process messages from this bot
    if not message.content.startswith(command_prefix):
        return  # If it's not a command, exit
    try:
        # Try to execute the command. If there's an error, log
        await misc.check_command(update_client=client, update_message=message)
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    console.init(client)


# Run the client
client.run(TOKEN)
