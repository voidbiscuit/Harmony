import discord
import re

# Final
charsToEscape = '\\*_`'

# Variables
client = discord.client
message = discord.message


# Check Commands
async def check_command(update_client, update_message):
    # Update Globals
    global client, message
    client = update_client
    message = update_message

    # Extract Data
    content = message.content.replace('t!', '')

    # Switch Commands
    if content.startswith('hello'):
        await reply(hello())
        return True

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


# Commands

# Reply Hello
def hello():
    return 'Hello {0.author.mention}'.format(message)


def penguin():
    return 'http://freegifmaker.me/img/res/1/5/4/7/9/2/15479246511996753.gif?1547924657'


# Escape
def escape(content):
    content = content.replace('escape', '', 1)
    for char in charsToEscape:
        content = content.replace(char, str.format("\\{:s}", char))
    return content


def pokecord_marketsearch(content):
    retval = str.format(
        'p!market search'
        ' --name {:s}'
        ' --order {:s}',
        content,
        'price ascending'
    )
    return retval


def english_to_russian(content):
    translation = {
        # Englishhian
        "Cat": "pushistiy",
        "Fluffy": "pushistiy",
        "Hello": "ПРИВЕТ",
        "Bear": "medved",
        "Anya": "Spoonya",
        "Tim": "Tim the Wizard",
        # Russian
        "ПРИВЕТ": "Hello"
    }
    for english, russian in translation.items():
        uppercase = content[0] > 'Z'
        pattern = re.compile(english, re.IGNORECASE)
        content = pattern.sub(russian, content)
    return content


# Invalid Command
def invalid_command():
    return '`Invalid Command`'


def whois(content):
    if content == "<@103865056172732416>":
        return "I'm a Wizard"
    if content == "<@285529910771056641>":
        return "I AM GERALT"
    return "Can't find u"
