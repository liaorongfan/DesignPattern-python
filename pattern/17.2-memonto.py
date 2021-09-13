from copy import deepcopy


class Memento:
    """备忘录"""

    def set_attributes(self, dict):
        """深度拷贝字典dict中的所有属性"""
        self.__dict__ = deepcopy(dict)

    def get_attributes(self):
        """获取属性字典"""
        return self.__dict__


class Caretaker:
    """备忘录管理类"""

    def __init__(self):
        self._mementos = {}

    def add_memento(self, name, memento):
        self._mementos[name] = memento

    def get_memento(self, name):
        return self._mementos[name]


class Originator:
    """备份发起人"""

    def create_memento(self):
        memento = Memento()
        memento.set_attributes(self.__dict__)
        return memento

    def restore_from_memento(self, memento):
        self.__dict__.update(memento.get_attributes())