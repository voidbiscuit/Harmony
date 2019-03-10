from MessageHandler.Command._Command import _Command


class Escape(_Command):

    def __init__(self):
        super(__class__, self).__init__()
        self.__characters_to_escape = '\\*_`'

    async def _execute(self, message):
        content = message.content
        for character in self.__characters_to_escape:
            content = content.replace(character, str.format("\\{:s}", character))
        return content
