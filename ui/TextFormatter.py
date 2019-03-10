# Default Values
import re


class TextUtils:
    def __init__(self, default_foreground=39, default_background=49):
        # Final
        self.__color_format = re.compile("^[0-9]{1,3}$")
        self.__default_foreground = default_foreground
        self.__default_background = default_background
        # Actual Values
        self.__current_foreground = self.__default_foreground
        self.__current_background = self.__default_background

    def __check_color(self, color):
        color = str(color)
        if self.__color_format.match(color):
            return color
        return ''

    def update_style(self, foreground, background):
        self.__current_foreground = foreground
        self.__current_background = background
        print(self.__text_format([self.__current_foreground, self.__current_background]))

    def reset_style(self):
        print(self.__text_format())

    def format_text(self, message, text_formats=91):
        message = str(message)
        if not isinstance(text_formats, type([])):
            text_formats = [text_formats]
        return self.__text_format(text_formats) + message + self.__text_format()

    def __text_format(self, text_formats=None):
        return_format = ''
        if text_formats is None:
            text_formats = [self.__default_foreground, self.__default_background]
        for text_format in text_formats:
            return_format += '\033[' + self.__check_color(text_format) + 'm'
        return return_format
