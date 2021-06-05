from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for o in self.__observers:
            print(f"实例对象来自{o.__class__}, 此对象使用它的update()方法，作用与参数{id(self)}")
            o.update(self)  # 注意这里的self 是函数update()的参数，不是对象的方法标识符


class WaterHeater(Observable):
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是：" + str(self.__temperature) + "℃")
        # 通知 观察者，只看当前 WaterHeater 类的信息
        self.notify_observers()


class WashingMode(Observer):
    """该模式用于洗澡用"""

    def update(self, observable_object):
        if 50 <= observable_object.get_temperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")
        else:
            print("洗澡模式没有更新")


class DrinkingMode(Observer):
    """该模式用于饮用"""

    def update(self, observable):
        if observable.get_temperature() >= 100:
            print("水已烧开！可以用来饮用了。")
        else:
            print("饮用模式没有更新")


def test_water_heater():
    heater = WaterHeater()
    print(f"实例化一个热水器对象,对象的id:{id(heater)}")
    washing_observer = WashingMode()
    drinking_observer = DrinkingMode()
    heater.add_observer(washing_observer)
    heater.add_observer(drinking_observer)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)


if __name__ == "__main__":
    test_water_heater()
