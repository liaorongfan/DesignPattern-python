# Version 2.0
# 代码框架
# ==============================
import os
from abc import ABCMeta, abstractmethod


# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法


class Component(metaclass=ABCMeta):
    """组件"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        # indent 仅用于内容输出时的缩进
        pass


class Composite(Component):
    """复合组件"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def isComposite(self):
        return True

    def feature(self, indent):
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)


class ComponentImplA(Component):
    """Test"""

    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print("name：%s" % self._name)


class FileDetail(Component):
    """谇详情"""

    def __init__(self, name):
        super().__init__(name)
        self._size = 0

    def setSize(self, size):
        self._size = size

    def getFileSize(self):
        return self._size

    def feature(self, indent):
        # 文件大小，单位：KB，精确度：2位小数
        fileSize = round(self._size / float(1024), 2)
        print("文件名称：%s， 文件大小：%sKB" % (self._name, fileSize))


class FolderDetail(Composite):
    """文件夹详情"""

    def __init__(self, name):
        super().__init__(name)
        self._count = 0

    def setCount(self, fileNum):
        self._count = fileNum

    def getCount(self):
        return self._count

    def feature(self, indent):
        print("文件夹名：%s， 文件数量：%d。包含的文件：" % (self._name, self._count))
        super().feature(indent)


def scanDir(rootPath, folderDetail):
    """扫描某一文件夹下的所有目录"""
    if not os.path.isdir(rootPath):
        raise ValueError("rootPath不是有效的路径：%s" % rootPath)

    if folderDetail is None:
        raise ValueError("folderDetail不能为空!")

    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(fileName)
            scanDir(filePath, folder)
            folderDetail.add_component(folder)
        else:
            fileDetail = FileDetail(fileName)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.add_component(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)


# Test
# ======================================================================================================================
def testComposite():
    tony = ComponentImplA("Tony")
    tony.feature()
    karry = ComponentImplA("Karry")
    composite = Composite("Composite")
    composite.addComponent(tony)
    composite.addComponent(karry)
    composite.feature()


def testDir():
    folder = FolderDetail("生活中的设计模式")
    scanDir("E:\生活中的设计模式", folder)
    folder.feature("")

    # isDir = os.path.isfile("D:\Test\file1.txt")
    # print(isDir)


# testComposite()
testDir()
