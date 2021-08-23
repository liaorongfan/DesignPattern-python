from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def get_name(self):
        return self._name

    def add_component(self, component, count=1, unit="个"):
        self.__components.append([component, count, unit])
        # print("%s 增加了 %d %s%s" % (self._name, count, unit, component) );

    @abstractmethod
    def feature(self):
        raise NotImplementedError


class Car(Toy):
    """小车"""

    def feature(self):
        print("我是 %s，我可以快速奔跑……" % self._name)


class Manor(Toy):
    """庄园"""

    def feature(self):
        print("我是 %s，我可供观赏，也可用来游玩！" % self._name)


class ToyBuilder(metaclass=ABCMeta):
    """玩具构建者"""

    @abstractmethod
    def build_product(self):
        pass


class CarBuilder(ToyBuilder):
    """车的构建类"""

    def build_product(self):
        car = Car("迷你小车")
        print("正在构建 %s ……" % car.get_name())
        car.add_component("轮子", 4)
        car.add_component("车身", 1)
        car.add_component("发动机", 1)
        car.add_component("方向盘")
        return car


class ManorBuilder(ToyBuilder):
    """庄园的构建类"""

    def build_product(self):
        manor = Manor("淘淘小庄园")
        print("正在构建 %s ……" % manor.get_name())
        manor.add_component('客厅', 1, "间")
        manor.add_component('卧室', 2, "间")
        manor.add_component("书房", 1, "间")
        manor.add_component("厨房", 1, "间")
        manor.add_component("花园", 1, "个")
        manor.add_component("围墙", 1, "堵")
        return manor


class BuilderMgr:
    """建构类的管理类"""

    def __init__(self):
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()

    def build_car(self, num):
        count = 0
        products = []
        while count < num:
            car = self.__carBuilder.build_product()
            products.append(car)
            count += 1
            print("建造完成第 %d 辆 %s" % (count, car.get_name()))
        return products

    def build_manor(self, num):
        count = 0
        products = []
        while count < num:
            manor = self.__manorBuilder.build_product()
            products.append(manor)
            count += 1
            print("建造完成第 %d 个 %s" % (count, manor.get_name()))
        return products


def test_advanced_builder():
    builderMgr = BuilderMgr()
    builderMgr.build_manor(2)
    print()
    builderMgr.build_car(4)


if __name__ == '__main__':
    test_advanced_builder()
