""" config.py """
# Created by. Present Jay (2020-07-24 ~)
# Table Definition Recognizer의 configure variable을 정의합니다. (constant)



# 디버깅 여부를 결정합니다 (False시 실행 중 에러를 최대한 배제함)
# False : ignore errors
DEBUG = True


# TEST 여부를 결정합니다
# test function을 작동할 때 체크합니다.
TEST = True


# Project code를 정의합니다.
PROJECTFILES = [
    'DirectoryManager.py',
    'CommandDecorator.py',
    'TDRmain.py',
    'TESTS.py',
    'config.py',
]


# Directory를 scan할 때, Project의 기본 file들을 ignore할 수 있도록 정의합니다.
IGNOREFILE_DEFAULT = [
    '__pycache__',
    '.gitignore',
    '.git',
    '.vscode',
    'venv',
    'README.md',
]


def unzip__projectfiles(obj):
    for _ in PROJECTFILES:
        obj.append(_)