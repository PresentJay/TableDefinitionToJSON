from DirectoryManager import *


""" TESTS.py """
# Created by. Present Jay (2020-07-24 ~)
# 각종 Function을 TEST하는 Function들을 정의합니다.


# list printing function
def printLists(_list, description=""):
    print('* *', description,'* *')
    if len(_list) > 0:
        for _ in _list: print('- ', _)
    else:
        print("this list is blank. . .")
    print()
        

        
# DirectoryManager의 getFiles Function을 테스트합니다
def getFilesTest():
    printLists(getFiles(), "Absolute Dirs")
    printLists(getFiles(absolute=False), "Relative Dirs")
    printLists(getFiles(extension='xlsx'), "Excel Absolute Dirs")
    printLists(getFiles(extension='xlsx', absolute=False), "Excel Relative Dirs")
