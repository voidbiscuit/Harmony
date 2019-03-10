from MessageHandler.Command.Commands.Escape import Escape
from MessageHandler.Command.Commands.Hello import Hello
from MessageHandler.Command.Commands.Pokecord import Pokecord
from MessageHandler.Command.Commands.Translation.Eng2Rus import Eng2Rus
from MessageHandler.Command.Commands.Translation.Rus2Eng import Rus2Eng
from MessageHandler.Command.Commands.Whois import Whois

commands = [
    # Default
    Hello(),
    # Generic
    Escape(),
    Pokecord(),
    Whois(),
    # Translation
    Eng2Rus(),
    Rus2Eng()
]
