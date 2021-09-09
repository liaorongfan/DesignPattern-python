from abc import ABCMeta, abstractmethod
import os


class Page:
    """电子书一页的内容"""
    def __init__(self, page_num):
        self.__page_num = page_num

    def get_content(self):
        return "第 " + str(self.__page_num) + " 页的内容..."


class Catalogue:
    """目录结构"""

    def __init__(self, title):
        self.__title = title
        self.__chapters = []

    def add_chapter(self, title):
        self.__chapters.append(title)

    def show_info(self):
        print("书名：" + self.__title)
        print("目录:")
        for chapter in self.__chapters:
            print("    " + chapter)


class IBook(metaclass=ABCMeta):
    """电子书文档的接口类"""

    @abstractmethod
    def parse_file(self, file_path):
        """解析文档"""
        pass

    @abstractmethod
    def get_catalogue(self):
        """获取目录"""
        pass

    @abstractmethod
    def get_page_count(self):
        """获取页数"""
        pass

    @abstractmethod
    def get_page(self, page_num):
        """获取第pageNum页的内容"""
        pass


class TxtBook(IBook):
    """TXT解析类"""

    def parse_file(self, file_path):
        # 模拟文档的解析
        print(file_path + " 文件解析成功")
        self.__title = os.path.splitext(file_path)[0]
        self.__page_count = 500
        return True

    def get_catalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.add_chapter("第一章 标题")
        catalogue.add_chapter("第二章 标题")
        return catalogue

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page_num):
        return Page(page_num)


class EpubBook(IBook):
    """Epub解析类"""

    def parse_file(self, file_path):
        # 模拟文档的解析
        print(file_path + " 文件解析成功")
        self.__title = os.path.splitext(file_path)[0]
        self.__page_count = 800
        return True

    def get_catalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.add_chapter("第一章 标题")
        catalogue.add_chapter("第二章 标题")
        return catalogue

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page_num):
        return Page(page_num)


class Outline:
    """第三方PDF解析库的目录类"""
    def __init__(self):
        self.__outlines = []

    def add_outline(self, title):
        self.__outlines.append(title)

    def get_outlines(self):
        return self.__outlines


class PdfPage:
    """PDF页"""

    def __init__(self, page_num):
        self.__page_num = page_num

    def get_page_num(self):
        return self.__page_num


class ThirdPdf:
    """第三方PDF解析库"""

    def __init__(self):
        self.__pageSize = 0
        self.__title = ""

    def open(self, file_path):
        print("第三方库解析PDF文件：" + file_path)
        self.__title = os.path.splitext(file_path)[0]
        self.__pageSize = 1000
        return True

    def get_title(self):
        return self.__title

    def get_outline(self):
        outline = Outline()
        outline.add_outline("第一章 PDF电子书标题")
        outline.add_outline("第二章 PDF电子书标题")
        return outline

    def page_size(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    """对第三方的PDF解析库重新进行包装"""

    def __init__(self, third_pdf):
        self.__third_pdf = third_pdf

    def parse_file(self, file_path):
        # 模拟文档的解析
        rtn = self.__third_pdf.open(file_path)
        if rtn:
            print(file_path + "文件解析成功")
        return rtn

    def get_catalogue(self):
        outline = self.get_outline()
        print("将Outline结构的目录转换成Catalogue结构的目录")
        catalogue = Catalogue(self.__third_pdf.get_title())
        for title in outline.get_outlines():
            catalogue.add_chapter(title)
        return catalogue

    def get_page_count(self):
        return self.__third_pdf.page_size()

    def get_page(self, page_num):
        page = self.page(page_num)
        print("将PdfPage的面对象转换成Page的对象")
        return Page(page.get_page_num())


class Reader:
    """阅读器"""

    def __init__(self, name):
        self.__name = name
        self.__file_path = ""
        self.__cur_book = None
        self.__cur_page_num = -1

    def __init_book(self, file_path):
        self.__file_path = file_path
        extName = os.path.splitext(file_path)[1]
        if extName.lower() == ".epub":
            self.__cur_book = EpubBook()
        elif extName.lower() == ".txt":
            self.__cur_book = TxtBook()
        elif extName.lower() == ".pdf":
            self.__cur_book = PdfAdapterBook(ThirdPdf())
        else:
            self.__cur_book = None

    def open_file(self, file_path):
        self.__init_book(file_path)
        if self.__cur_book is not None:
            rtn = self.__cur_book.parse_file(file_path)
            if rtn:
                self.__cur_page_num = 1
            return rtn
        return False

    def close_file(self):
        print("关闭 " + self.__file_path + " 文件")
        return True

    def show_catalogue(self):
        catalogue = self.__cur_book.get_catalogue()
        catalogue.show_info()

    def pre_page(self):
        print("往前翻一页：", end="")
        return self.goto_page(self.__cur_page_num - 1)

    def next_page(self):
        print("往后翻一页：", end="")
        return self.goto_page(self.__cur_page_num + 1)

    def goto_page(self, page_num):
        if 1 < page_num < self.__cur_book.get_page_count() -1:
            self.__cur_page_num = page_num

        print("显示第" + str(self.__cur_page_num) + "页")
        page = self.__cur_book.get_page(self.__cur_page_num)
        page.get_content()
        return page


def testReader():
    reader = Reader("阅读器")
    if not reader.open_file("平凡的世界.txt"):
        return
    reader.show_catalogue()
    reader.pre_page()
    reader.next_page()
    reader.next_page()
    reader.close_file()
    print()

    if not reader.open_file("追风筝的人.epub"):
        return
    reader.show_catalogue()
    reader.next_page()
    reader.next_page()
    reader.pre_page()
    reader.close_file()
    print()

    if not reader.open_file("如何从生活中领悟设计模式.pdf"):
        return
    reader.show_catalogue()
    reader.next_page()
    reader.next_page()
    reader.close_file()


if __name__ == '__main__':
    testReader()

