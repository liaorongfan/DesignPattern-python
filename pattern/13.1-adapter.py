"""
set a adapter to change British socket to Chinese socket.
"""

from abc import ABCMeta, abstractmethod


class SocketEntity:
    """接口类型定义"""

    def __init__(self, pin_num, pin_type):
        self.__pin_num = pin_num
        self.pin_type = pin_type

    def get_pin_num(self):
        return self.__pin_num

    def set_pin_num(self, pin_num):
        self.__pin_num = pin_num

    def get_pin_type(self):
        return self.pin_type

    def set_pin_type(self, pin_type):
        self.pin_type = pin_type


class ISocket(metaclass=ABCMeta):
    """插座类型"""

    def get_name(self):
        """插座名称"""
        pass

    def get_socket(self):
        """获取接口"""
        pass


class ChineseSocket(ISocket):
    """国标插座"""

    def get_name(self):
        return "国标插座"

    def get_socket(self):
        return SocketEntity(3, "八字扁型")


class BritishSocket:
    """英标插座"""

    def name(self):
        return "英标插座"

    def socket_interface(self):
        return SocketEntity(3, "T字方型")


class AdapterSocket(ISocket):
    """插座转换器"""

    def __init__(self, british_socket):
        self.__british_socket = british_socket  # object

    def get_name(self):
        return self.__british_socket.name() + "转换器"

    def get_socket(self):
        socket = self.__british_socket.socket_interface()  # socket: object of class SocketEntity
        socket.set_pin_type("八字扁型")
        return socket


def can_charge_for_digital_device(name, socket):
    if socket.get_pin_num() == 3 and socket.get_pin_type() == "八字扁型":
        is_standard = "符合"
        can_charge = "可以"
    else:
        is_standard = "不符合"
        can_charge = "不能"

    print("[%s]：\n针脚数量：%d，针脚类型：%s； %s中国标准，%s给大陆的电子设备充电！"
          % (name, socket.get_pin_num(), socket.get_pin_type(), is_standard, can_charge))


def testSocket():
    chineseSocket = ChineseSocket()
    can_charge_for_digital_device(chineseSocket.get_name(), chineseSocket.get_socket())

    britishSocket = BritishSocket()
    can_charge_for_digital_device(britishSocket.name(), britishSocket.socket_interface())

    adapterSocket = AdapterSocket(britishSocket)
    can_charge_for_digital_device(adapterSocket.get_name(), adapterSocket.get_socket())


if __name__ == '__main__':
    testSocket()
