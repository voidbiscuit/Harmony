class _Command:

    def __init__(self):
        self.__command = type(self).__name__

    async def execute(self, command, message):
        if str(self.__command).lower() == str(command).lower():
            return await self._execute(message)
        return None

    @staticmethod
    async def _execute(message):
        return "Error"
