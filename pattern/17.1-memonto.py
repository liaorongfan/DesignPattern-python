class Engineer:
    """工程师"""

    def __init__(self, name):
        self.__name = name
        self.__work_items = []

    def add_work_item(self, item):
        self.__work_items.append(item)

    def forget(self):
        self.__work_items.clear()
        print(self.__name + "工作太忙了，都忘记要做什么了！")

    def write_List(self):
        """将工作项记录TodoList"""
        todoList = TodoList()
        for item in self.__work_items:
            todoList.write_work_item(item)
        return todoList

    def retrospect(self, todoList):
        """回忆工作项"""
        self.__work_items = todoList.get_work_items()
        print(self.__name + "想起要做什么了！")

    def show_item(self):
        if len(self.__work_items):
            print(self.__name + "的工作项：")
            for idx in range(0, len(self.__work_items)):
                print(str(idx + 1) + ". " + self.__work_items[idx] + ";")
        else:
            print(self.__name + "暂无工作项！")


class TodoList:
    """工作项"""

    def __init__(self):
        self.__work_items = []

    def write_work_item(self, item):
        self.__work_items.append(item)

    def get_work_items(self):
        return self.__work_items


class TodoListCaretaker:
    """TodoList管理类"""

    def __init__(self):
        self.__todoList = None

    def set_todo_list(self, todoList):
        self.__todoList = todoList

    def getTodoList(self):
        return self.__todoList


def test_engineer():
    tony = Engineer("Tony")
    tony.add_work_item("解决线上部分用户因昵称太长而无法显示全的问题")
    tony.add_work_item("完成PDF的解析")
    tony.add_work_item("在阅读器中显示PDF第一页的内容")
    tony.show_item()
    caretaker = TodoListCaretaker()
    caretaker.set_todo_list(tony.write_List())

    print()
    tony.forget()
    tony.show_item()

    print()
    tony.retrospect(caretaker.getTodoList())
    tony.show_item()


if __name__ == '__main__':
    test_engineer()
