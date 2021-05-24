"""Translation package"""

from excepts import TranslatorException


TRANSLATORS = {
    "Google translator": "gt",
    "Microsoft translator": "mt",
    "Yandex translator": "yt",
    "Linguee translator": "lt",
    "MyMemory translator": "mmt",
    "Pons translator": "pt",
}


def supported_langs(translator) -> list:
    if translator in TRANSLATORS.keys() or translator in TRANSLATORS.values():
        if translator == "Google translator" or translator == "gt":
            pass
        elif translator == "Microsoft translator" or translator == "mt":
            pass
        elif translator == "Yandex translator" or translator == "yt":
            pass
    else:
        raise TranslatorException(f'The translator "{translator}" has not been found')
