# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import xlrd as xl

from py_utils.excel.excel_base import ExcelBase


class Passer(ExcelBase):
    def __init__(self, file):
        ExcelBase.__init__(self, file)
        self.__sheet = None
        self.__row = None
        self.__excel = xl.open_workbook(self.file)
        print("file is ", self.__excel)

    def seek_sheet(self, sheet_index):
        self.__sheet = self.__excel.sheets()[sheet_index]
        return self

    def seek_row(self, row_num):
        self.__row = self.__sheet.row_values(row_num)
        return self

    def seek_cell(self, row_num, colum_num):
        self.seek_row(row_num)
        return self.row()[colum_num]

    def row(self):
        return self.__row

    def rows(self):
        return self.__sheet.get_rows()
