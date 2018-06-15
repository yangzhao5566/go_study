# coding=utf-8
import xlrd


class ExcelReader(object):
    """读取文件"""
    def __init__(self, path, start_row=1, sheet_index=0):
        self._path = path
        self._book = xlrd.open_workbook(path)
        self._sheet = self._book.sheet_by_index(sheet_index)
        self.row = start_row
        self.max_column = self._sheet.ncols
        self._finish = False
        self.dict = []
        for i in range(self.max_column):
            val = self._sheet.cell_value(rowx=0, colx=i)
            self.dict.append(val)
        print(self.dict)

    def _read_line(self):
        columns = {}
        for col in range(0, self.max_column + 1):
            try:
                val = self._sheet.cell_value(rowx=self.row, colx=col)
            except IndexError:
                # 如果第一列无值则认为读取到文件末尾
                if col == 0:
                    self._finish = True
                break
            if isinstance(val, (int, float)):
                val = unicode(int(val))
            key = self.dict[col]
            columns[key] = val
        return columns

    def __iter__(self):
        """迭代返回每一行"""
        while not self._finish:
            yield self._read_line()
            self.row += 1


excl = ExcelReader("/Users/yz/Desktop/djs_show/data_show/who_en_set.xlsx")

if __name__ == "__main__":
    for one in excl:
        print(one)
