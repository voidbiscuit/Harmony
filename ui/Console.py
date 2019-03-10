import datetime

# Text Colours
import discord

from ui.TextFormatter import TextUtils


class Console:
    def __init__(self, text_formatter):
        self.__text_formatter = text_formatter
        self.__timestamp_format = '%Y/%m/%d %H:%M:%S'
        self.__initialised = False

    def format_message(self, message):
        line = str.format(
            '{:50s} | {:s}',  # Prefix | Message
            str.format(
                '{:s} {:s} {:s}',
                datetime.datetime.strftime(message.timestamp, self.__timestamp_format),
                message.server.name,
                message.author.id
            ),
            str.format(
                '{:s} : {:s}',
                message.author.name,
                message.content
            )
        )
        if message.author.bot:
            line = self.__text_formatter.format_text(line)
        return line

    def start_message(self, client):
        if self.__initialised:
            return
        self.__initialised = True
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
