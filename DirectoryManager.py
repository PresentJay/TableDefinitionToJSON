import os.path


""" DirectoryManager.py """
# Created by. Present Jay (2020-07-24 ~)
# 특정 Directory의 File들을 가져오는 등, Directory Address에 관한 사항을 관리하는 Function을 정의합니다.


def getFiles(absolute=True):
    files = []
    if absolute:
        _dir = os.getcwd()
        for _file in os.listdir(_dir):
            files.append(os.path.join(_dir, _file))
    else:
        files = os.listdir(os.getcwd())
    return files


