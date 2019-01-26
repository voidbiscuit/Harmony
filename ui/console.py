import datetime
import discord


def print_message(message):
    line = str.format(
        # Format
        '[{:s}] {:18s} || '  # Timestamp
        '{:>32s} : {:s}',  # Message
        # Data
        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        message.author.id,
        message.author.name,
        message.content
    )
    if message.author.bot:
        line = __bot_message(line)
    return line


def __bot_message(message):
    return str.format(
        # Format
        '{:s}{:s}{:s}'
        # Vals
        '\033[91m',  # Set Red
        message,  # Message
        '\033[0m'  # Set Normal
    )


def init(client):
    # Init
    print(str.format(
        '\n' * 100 +
        '\n-'
        '\n- Logged in as {:s} user ID {:s}'
        '\n-'
        '\n- The time is now {:s}',
        client.user.name,
        client.user.id,
        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    ))
    # Listening
    print(
        '\n\n\n'
        '\n- Listening for Commands'
        '\n\n'
    )
