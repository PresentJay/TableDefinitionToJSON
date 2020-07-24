from DirectoryManager import *


""" TESTS.py """
# Created by. Present Jay (2020-07-24 ~)
# 각종 Function을 TEST하는 Function들을 정의합니다.


# Coded by. PresentJay
# 2020-07-24 ~ (PROCEEDING)
# DirectoryManager의 getFiles Function을 테스트합니다
def getFilesTest():
    print('* * absolute dir__')
    for _ in getFiles():
        print('- ', _)
    print('* * relative dir__')
    for _ in getFiles(False):
        print('- ', _)
