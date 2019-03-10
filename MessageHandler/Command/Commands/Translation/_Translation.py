import re

from MessageHandler.Command._Command import _Command


class _Translation(_Command):

    def __init__(self):
        super(__class__, self).__init__()
        self._set_translation({})

    def _set_translation(self, translation):
        self.__translation = translation

    async def _execute(self, message):
        reply = message.content
        for from_word, to_word in self.__translation.items():
            pattern = re.compile(from_word, re.IGNORECASE)
            reply = pattern.sub(to_word, reply)
        return reply
