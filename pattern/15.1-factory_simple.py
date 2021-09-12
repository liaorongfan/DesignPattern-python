from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    """咖啡"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_taste(self):
        pass


class LatteCaffe(Coffee):
    """拿铁咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def get_taste(self):
        return "轻柔而香醇"


class MochaCoffee(Coffee):
    """摩卡咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def get_taste(self):
        return "丝滑与醇厚"


class Coffeemaker:
    """咖啡机"""

    @staticmethod
    def make_coffee(coffee_bean):
        if coffee_bean == "拿铁咖啡豆":
            coffee = LatteCaffe("拿铁咖啡")
        elif coffee_bean == "摩卡咖啡豆":
            coffee = MochaCoffee("摩卡咖啡")
        else:
            raise ValueError(f"不支持的参数：{coffee_bean}")
        return coffee


def test_coffee_maker():
    latte = Coffeemaker.make_coffee("拿铁咖啡豆")
    print("{} 已为您准备好了，口感：{}。请慢慢享用！".format(latte.get_name(), latte.get_taste()))
    mocha = Coffeemaker.make_coffee("摩卡咖啡豆")
    print("{} 已为您准备好了，口感：{}。请慢慢享用！".format(mocha.get_name(), mocha.get_taste()))


if __name__ == '__main__':
    test_coffee_maker()
