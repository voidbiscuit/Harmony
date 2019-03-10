from MessageHandler.Command.Commands.Translation._Translation import _Translation


class Eng2Rus(_Translation):

    def __init__(self):
        super(__class__, self).__init__()
        self._set_translation({
            "Cat": "pushistiy",
            "Fluffy": "pushistiy",
            "Hello": "ПРИВЕТ",
            "Bear": "medved",
            "Anya": "Spoonya",
            "Tim": "Tim the Wizard"
        })
