import config
if config.TEST:
    from TESTS import *
else:
    from DirectoryManager import *
    import click
    import six
    from PyInquirer import Token, prompt, style_from_dict, Separator
    from pyfiglet import figlet_format
    try:
        import colorama
        colorama.init()
    except ImportError:
        colorama = None
    try:
        from termcolor import colored
    except ImportError:
        colored = None


""" TDRmain.py """
# Created by. Present Jay (2020-07-24 ~)
# Table Definition Recognizer의 main을 작성합니다.


def main():
    # getFilesTest()
    CommandLoopTest()


if __name__ == "__main__":
    main()