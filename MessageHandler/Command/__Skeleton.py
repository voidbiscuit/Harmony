from MessageHandler.Command._Command import _Command


class Skeleton(_Command):

    def __init__(self):
        super(__class__, self).__init__()

    async def _execute(self, message):
        return None
