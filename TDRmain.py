import config
if config.TEST:
    from TESTS import *
else:
    from DirectoryManager import *


""" TDRmain.py """
# Created by. Present Jay (2020-07-24 ~)
# Table Definition Recognizer의 main을 작성합니다.


def main():
    getFilesTest()


if __name__ == "__main__":
    main()