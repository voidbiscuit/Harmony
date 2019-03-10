from MessageHandler.Command._Command import _Command


class Hello(_Command):

    def __init__(self):
        super(__class__, self).__init__()

    async def _execute(self, message):
        return 'Hello {0.author.mention}'.format(message)
