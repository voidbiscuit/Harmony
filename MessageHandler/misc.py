import discord
import re



# Variables
client = discord.client
message = discord.message


# Check Command
async def check_command(update_client, update_message):
    # Update Globals
    global client, message
    client = update_client
    message = update_message

    # Extract Data
    content = message.content.replace('t!', '')

    # Switch Command


    if content.startswith('penguin'):
        await reply(penguin())
        return True

    if content.startswith('escape'):
        await reply(escape(content))
        return True

    if content.startswith('marketsearch'):
        content = content.replace('marketsearch', '')
        await reply(pokecord_marketsearch(content))
        return True

    if (content.startswith("russia")):
        content = content.replace('russia', '', 1)
        await reply(english_to_russian(content))
        return True
        # Replace Clever Russian

    if (content.startswith("whois")):
        content = content.replace('whois ', '', 1)
        await reply(whois(content))
        return True

    await reply(invalid_command())
    return False


# Send Replies
async def reply(response):
    global client, message
    await client.send_message(
        message.channel,
        response
    )


# Command

# Reply Hello
def hello():



def penguin():
    return 'http://freegifmaker.me/img/res/1/5/4/7/9/2/15479246511996753.gif?1547924657'


# Escape
def escape(content):



def pokecord_marketsearch(content):
    retval =
    return retval