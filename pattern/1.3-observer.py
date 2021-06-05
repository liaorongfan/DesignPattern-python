from abc import ABCMeta, abstractmethod
import time


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

    def notify_observers(self, the_object):
        for o in self.__observers:
            o.update(self, the_object)
            # print(id(self))


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latest_ip = {}
        self.__latest_region = {}

    def login(self, name, ip, log_time):
        region = self.__get_region(ip)
        if self.__isLongDistance(name, region):
            self.notify_observers({"name": name, "ip": ip, "region": region, "time": log_time})
        self.__latest_region[name] = region
        self.__latest_ip[name] = ip

    @staticmethod
    def __get_region(ip):
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
        latestRegion = self.__latest_region.get(name)
        return latestRegion is not None and latestRegion != region;


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, the_object):
        print("[短信发送] " + the_object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + the_object["region"] + "  登录ip：" + the_object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(the_object["time"])))


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, the_object):
        print("[邮件发送] " + the_object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + the_object["region"] + "  登录ip：" + the_object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(the_object["time"])))


def test_login():
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())
    account.login("Tony", "101.47.18.9", time.time())
    account.login("Tony", "67.218.147.69", time.time())


if __name__ == "__main__":
    test_login()
