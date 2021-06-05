##!/usr/bin/python

# Version 1.0
########################################################################################################################
# from abc import ABCMeta, abstractmethod
# # 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
#
# class WaterHeater:
#     """热水器：战胜寒冬的有利武器"""
#
#     def __init__(self):
#         self.__observers = []
#         self.__temperature = 25
#
#     def getTemperature(self):
#         return self.__temperature
#
#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         print("当前温度是：" + str(self.__temperature) + "℃")
#         self.notifies()
#
#     def addObserver(self, observer):
#         self.__observers.append(observer)
#
#     def notifies(self):
#         for o in self.__observers:
#             o.update(self)
#
#
# class Observer(metaclass=ABCMeta):
#     "洗澡模式和饮用模式的父类"
#
#     @abstractmethod
#     def update(self, waterHeater):
#         pass
#
#
# class WashingMode(Observer):
#     """该模式用于洗澡"""
#
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
#             print("水已烧好！温度正好，可以用来洗澡了。")
#
#
# class DrinkingMode(Observer):
#     """该模式用于饮用"""
#
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 100:
#             print("水已烧开！可以用来饮用了。")


# Version 2.0
########################################################################################################################
from abc import ABCMeta, abstractmethod


# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, the_object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, the_object=0):
        for o in self.__observers:
            o.update(self, the_object)
            print(id(self))


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
        self.notify_observers()


class WashingMode(Observer):
    """该模式用于洗澡用"""

    def update(self, observable, the_object):
        if isinstance(observable, WaterHeater) \
                and 50 <= observable.get_temperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    """该模式用于饮用"""

    def update(self, observable, objects):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 100:
            print("水已烧开！可以用来饮用了。")


import time
# 导入时间处理模块


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notify_observers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取地区信息。这里只是模拟，真实项目中应该调用IP地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录的地区差距。
        # 这里只是简单地用字符串匹配来模拟，真实的项目中应该调用地理信息相关的服务
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region;


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, objects):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def test_water_heater():
    heater = WaterHeater()
    washing_observer = WashingMode()
    drinking_observer = DrinkingMode()
    heater.add_observer(washing_observer)
    heater.add_observer(drinking_observer)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)


def test_login():
    accout = Account()
    accout.add_observer(SmsSender())
    accout.add_observer(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    accout.login("Tony", "67.218.147.69", time.time())


def test_time():
    print(time.time())
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    print(strTime)


if __name__ == "__main__":
    test_water_heater()
    # test_login()

    # testTime()

    # ipRegion = {
    #             "101.47.18.9": "浙江省杭州市",
    #             "67.218.147.69":"美国洛杉矶"
    #         }
    #
    # print(ipRegion["101.47.18.90"])
