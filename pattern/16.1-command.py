from abc import ABCMeta, abstractmethod


class Chief():
    """厨师"""

    def steam_food(self, original_material):
        print("%s清蒸中..." % original_material)
        return "清蒸" + original_material

    def fried_food(self, original_material):
        print("%s爆炒中..." % original_material)
        return "香辣炒" + original_material


class Order(metaclass=ABCMeta):
    """订单"""

    def __init__(self, name, original_material):
        self._chef = Chief()
        self._name = name
        self._original_material = original_material

    def get_display_name(self):
        return self._name + self._original_material

    @abstractmethod
    def processing_order(self):
        pass


class SteamedOrder(Order):
    """清蒸"""

    def __init__(self, original_material):
        super().__init__("清蒸", original_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.steam_food(self._original_material)
        return ""


class SpicyOrder(Order):
    """香辣炒"""

    def __init__(self, original_material):
        super().__init__("香辣炒", original_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.fried_food(self._original_material)
        return ""


class Waiter:
    """服务员"""

    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receive_order(self, order):
        self.__order = order
        print("服务员%s：您的 %s 订单已经收到,请耐心等待" % (self.__name, order.get_display_name()))

    def place_order(self):
        food = self.__order.processing_order()
        print("服务员%s：您的餐 %s 已经准备好，请您慢用!" % (self.__name, food))


def test_order():
    waiter = Waiter("Anna")
    steamedOrder = SteamedOrder("大闸蟹")
    print("客户David：我要一份 %s" % steamedOrder.get_display_name())
    waiter.receive_order(steamedOrder)
    waiter.place_order()
    print()

    spicyOrder = SpicyOrder("大闸蟹")
    print("客户Tony：我要一份 %s" % spicyOrder.get_display_name())
    waiter.receive_order(spicyOrder)
    waiter.place_order()


if __name__ == "__main__":
    test_order()
