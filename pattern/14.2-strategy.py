from abc import ABCMeta, abstractmethod


class Person:
    """人类"""

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show_myself(self):
        print("%s 年龄：%d岁，体重：%0.2fkg，身高：%0.2fm" % (self.name, self.age, self.weight, self.height) )


class ICompare(metaclass=ABCMeta):
    """比较算法"""

    @abstractmethod
    def comparable(self, person1, person2):
        """person1 > person2 返回值>0，person1 == person2 返回0， person1 < person2 返回值小于0"""
        pass


class CompareByAge(ICompare):
    """通过年龄排序"""

    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    """通过身高进行排序"""

    def comparable(self, person1, person2):
        return person1.height - person2.height


class CompareByHeightAndWeight(ICompare):
    """根据身高和体重的综合情况来排序
    (身高和体重的权重分别是0.6和0.4)"""

    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2


class SortPerson:
    """Person的排序类"""

    def __init__(self, compare):
        self.__compare = compare

    def sort(self, person_list):
        """排序算法
        这里采用最简单的冒泡排序"""
        n = len(person_list)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if self.__compare.comparable(person_list[j], person_list[j + 1]) > 0:
                    tmp = person_list[j]
                    person_list[j] = person_list[j + 1]
                    person_list[j + 1] = tmp
            j += 1
        i += 1


def test_sort_person():
    person_list = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 31, 74.5, 1.80),
        Person("Nick", 54, 44.5, 1.59),
        Person("Eric", 23, 62.0, 1.78),
        Person("Helen", 16, 45.7, 1.60)
    ]
    ageSorter = SortPerson(CompareByAge())
    ageSorter.sort(person_list)
    print("根据年龄进行排序后的结果：")
    for person in person_list:
        person.show_myself()
    print()

    heightSorter = SortPerson(CompareByHeight())
    heightSorter.sort(person_list)
    print("根据身高进行排序后的结果：")
    for person in person_list:
        person.show_myself()
    print()


if __name__ == '__main__':
    test_sort_person()
