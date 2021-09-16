from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    """享元类"""

    @abstractmethod
    def operation(self, extrinsicState):
        pass


class FlyweightImpl(Flyweight):
    """享元类的具体实现类"""

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsic_state):
        print("%s 取得 %s色颜料" % (extrinsic_state, self.__color))


class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self.__flyweights = {}

    def getFlyweight(self, key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment

