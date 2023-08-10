import json
from math import fabs
import os
import string
from unittest.mock import patch


def loadConfig():
    '''
    加载配置文件
    '''
    if os.path.exists('Config.json') == 0:
        return None
    with open("Config.json","r") as config_file:
        config_dict = json.load(config_file)
        return config_dict


def readLines(filepath):
    '''
    读取文件中的所有行
    '''
    if os.path.exists(filepath):
        readFile = open(filepath)
        lines =readFile.readlines()
        readFile.close()
        files = []
        for  l in lines:
            files.append(l.rstrip())
        return files 
    else :
        print("WARNING:",filepath,"is not exists!")
        return []


def getallfilesOfdir(dir:string,match:list):
    '''
    获得某个目录下匹配的文件
    '''
    # os.chdir(self.config["directorypath"])
    # print(os.path.abspath(os.curdir))
    all_file = os.listdir(dir)
    files = []
    for f in all_file:
        path = dir +"\\" +f # 使用全路径判断是文件还是文件夹
        # print(f,"isdir ：",os.path.isdir(path),"    isfile ：",os.path.isfile(path))

        if os.path.isdir(path):
            files.extend(getallfilesOfdir(path,match))
        else:
            # 获得后缀，不包括.
            suffix =  os.path.splitext(path)[-1].removeprefix('.')
            if suffix in match:
                files.append(path)
    return files