"""Exception"""


class TranslatorException(Exception):
    """TranslatorException"""

    def __init__(self, error_type):
        super(TranslatorException, self).__init__(error_type)
