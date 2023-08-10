
from importlib.metadata import files
from Tools import getallfilesOfdir, readLines

class ModeBase:

    #config
    config = None
 

    def __init__(self,config) -> None:
        self.config = config

    # 获取文件路径
    def getFilesPath(self):
        pass


class ModeDirectory(ModeBase):

    def __init__(self, config) -> None:
        super().__init__(config)

    def getFilesPath(self):
       return getallfilesOfdir(self.config["directorypath"],self.config["include"])


class ModeFiles(ModeBase):
    def __init__(self, config) -> None:
        super().__init__(config)

    def getFilesPath(self):
       animPaths = readLines( self.config["filespath"]) #所有要处理文件的相对路径 assets\...
       # 相对路径加上 项目工程路径
       files = []
       for line in  animPaths:
           files.append(self.config["projectpath"] + line)
       return files
    