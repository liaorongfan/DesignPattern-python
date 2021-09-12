from abc import ABCMeta, abstractmethod
from enum import Enum


class PenType(Enum):
    """画笔类型"""
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    """画笔"""

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def get_type(self):
        pass

    def get_name(self):
        return self.__name


class LinePen(Pen):
    """直线画笔"""

    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.PenTypeLine


class RectanglePen(Pen):
    """矩形画笔"""

    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    """椭圆画笔"""

    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.PenTypeEllipse


class PenFactory:
    """画笔工厂类"""

    def __init__(self):
        """定义一个字典(key:PenType，value：Pen)来存放对象,确保每一个类型只会有一个对象"""
        self.__pens = {}

    def get_single_obj(self, penType, name):
        """获得唯一实例的对象"""

    def create_pen(self, penType):
        """创建画笔"""
        # 如果该对象不存在，则创建一个对象并存到字典中
        if self.__pens.get(penType) is None:
            if penType == PenType.PenTypeLine:
                pen = LinePen("直线画笔")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("矩形画笔")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("椭圆画笔")
            else:
                pen = Pen("")
            self.__pens[penType] = pen
        # 否则直接返回字典中的对象
        return self.__pens[penType]


def test_pen_factory():
    factory = PenFactory()
    linePen = factory.create_pen(PenType.PenTypeLine)
    print("创建了 %s，对象id：%s， 类型：%s" % (linePen.get_name(), id(linePen), linePen.get_type()))
    rectPen = factory.create_pen(PenType.PenTypeRect)
    print("创建了 %s，对象id：%s， 类型：%s" % (rectPen.get_name(), id(rectPen), rectPen.get_type()))
    rectPen2 = factory.create_pen(PenType.PenTypeRect)
    print("创建了 %s，对象id：%s， 类型：%s" % (rectPen2.get_name(), id(rectPen2), rectPen2.get_type()))
    ellipsePen = factory.create_pen(PenType.PenTypeEllipse)
    print("创建了 %s，对象id：%s， 类型：%s" % (ellipsePen.get_name(), id(ellipsePen), ellipsePen.get_type()))


if __name__ == '__main__':
    test_pen_factory()
