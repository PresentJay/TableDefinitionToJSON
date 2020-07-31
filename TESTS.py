from DirectoryManager import *
from CommandDecorator import *
from TableDefinitionManager import *


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


# CommandDecorator의 process를 테스트합니다
def commandTest():
    questions = listQ(
        message="Select Excel File >> ",
        name="excel",
        choicelist=getFiles(extension='xlsx', absolute=False),
        exitloop=True
    )
    
    answers = prompt(questions, style=style)
    return answers

# CommandTest를 loop환경으로 Test합니다.
def CommandLoopTest():
    while(True):
        # clear terminal code
        print(u"{}[2J{}[;H".format(chr(27), chr(27)), end="")

        log("T.D.R", color="magenta", figlet=True)
        log("Table Definition Recognizer by Python Client.", "green")
        log("\t\t\t-dev PresentJay, 20.07", "yellow")
        print("\n")

        DTOJpycl = commandTest()
        if DTOJpycl.get('exit_confirm'):
            break
        
        read_TableDefinition(DTOJpycl.get('excel'))