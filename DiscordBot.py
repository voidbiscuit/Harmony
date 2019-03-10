import os
import time
import webbrowser

import discord

from MessageHandler.MessageHandler import MessageHandler
from ui.Console import Console
from ui.TextFormatter import TextUtils


# noinspection PyTypeChecker
class DiscordBot:
    def __init__(self):
        self.__text_util = TextUtils()
        print("\n\n")

        # Data Directories
        self.config_path = 'config/'
        self.config = {
            'prefix': None,
            'token': None
        }
        self.__init_files()
        # Data
        self.__command_prefix = self.config['prefix']
        self.__token = self.config['token']

        # Objects
        self.__console = Console(self.__text_util)
        # Discord Client
        self.__client = discord.Client()
        self.__message_handler = MessageHandler(self.__client, self.__console, self.__command_prefix)

        # Initialise
        self.__set_style()
        self.__set_client_events()

        # Run the client
        if self.__token is not None:
            self.__client.run(self.__token)
        else:
            print("Token is Invalid")

    def __set_style(self, foreground=96, background=100):
        self.__text_util.update_style(foreground, background)

    def __set_client_events(self):
        # Initialise Discord Client
        client = self.__client

        @client.event
        async def on_ready():
            self.__console.start_message(client)

        @client.event
        async def on_message(message):
            # Process Message
            response = await self.__message_handler.process_message(message)
            if response is not None:
                await client.send_message(message.channel, response)

    def __init_files(self):
        # Create Dir
        if not os.path.isdir(self.config_path):
            os.mkdir(self.config_path)
        # Create Config Files
        for config_name, config_values in self.config.items():
            file_path = self.config_path + config_name + '.txt'
            if not os.path.isfile(file_path):
                open(file_path, 'w').write('')
        # Read Files
        for file in os.listdir(self.config_path):
            if file.endswith('.txt'):
                self.config.update({file.split('.')[-2]: open(self.config_path + file, 'r').read()})
        # If token is empty, get user token
        while self.config['token'] == '':
            print(self.__text_util.format_text(open('Instructions/empty_token_file.txt').read(), [34]))
            input("\nPress Enter to open WebPage")
            webbrowser.open('https://discordapp.com/developers/applications/')
            token = input(self.__text_util.format_text('\nToken > ', [34]))
            self.config.update({'token': token})
            open(self.config_path + 'token.txt', 'w').write(token.strip('\\s'))

        while self.config['prefix'] == '':
            prefix = ''
            confirm = ''
            while not confirm[:3].lower() == 'yes':
                prefix = ''
                while prefix == '':
                    prefix = input(self.__text_util.format_text('\nEnter Prefix > ', [34]))
                confirm = input('Prefix will be set as [' + prefix + ']\nIs this okay? Type Yes to confirm. > ')
            self.config.update({"prefix": prefix})
            open(self.config_path + 'prefix.txt', 'w').write(prefix)
