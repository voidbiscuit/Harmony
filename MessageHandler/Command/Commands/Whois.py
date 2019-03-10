from MessageHandler.Command._Command import _Command


class Whois(_Command):

    def __init__(self):
        super(__class__, self).__init__()

    async def _execute(self, message):
        content = message.content
        if content == "<@103865056172732416>":
            return "I'm a Wizard"
        if content == "<@285529910771056641>":
            return "I AM GERALT"
        return "Can't find u"
