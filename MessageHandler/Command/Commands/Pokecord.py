from MessageHandler.Command._Command import _Command


class Pokecord(_Command):

    def __init__(self):
        super(__class__, self).__init__()

    async def _execute(self, message):
        content = str(message.content)
        if content.startswith('marketsearch'):
            content = content[len('marketsearch') + 1:]
            return str.format(
                'p!market search \\ \n'
                ' --name {:s} \\ \n'
                ' --order {:s}\\ \n',
                content,
                'price ascending'
            )
