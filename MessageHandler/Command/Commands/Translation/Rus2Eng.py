from MessageHandler.Command.Commands.Translation._Translation import _Translation


class Rus2Eng(_Translation):

    def __init__(self):
        super(__class__, self).__init__()
        self._set_translation({
            "ПРИВЕТ": "Hello"
        })
