from config.commands import commands


class MessageHandler:
    def __init__(self, client, console, command_prefix):
        # Objects
        self.__console = console
        self.__client = client
        # Values
        self.__command_prefix = command_prefix
        self.__commands = commands
        # Get Command

    async def process_message(self, message):
        result = None
        # If the message isn't from another bot
        if not message.author.bot or message.author is self.__client.user:
            print(self.__console.format_message(message))
            if message.author is not self.__client.user:
                command = self.__check_command(message)
                if command is not None:
                    message.content = message.content[len(self.__command_prefix) + len(command) + 1:]
                    result = await self.__execute_commands(command, message)
        return result

    def __check_command(self, message):
        # Init
        command = None
        content = str(message.content)
        # Check if message is a command
        if content.startswith(self.__command_prefix):
            # Remove the prefix, and get the command
            content = content[len(self.__command_prefix):]
            command = content.split(' ')[0]
        return command

    async def __execute_commands(self, command, message):
        for check_command in self.__commands:
            result = await check_command.execute(command, message)
            if result is not None:
                return result
        return None
