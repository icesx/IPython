# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import xlwt as xl

from py_utils.excel.excel_base import ExcelBase


class Writer(ExcelBase):
    def __init__(self,file):
        ExcelBase.__init__(self,file)
        self.__workbook = xl.Workbook()
        self.__sheet = None

    def add_sheet(self,sheet_name):
        self.__sheet = self.__workbook.add_sheet(sheet_name,cell_overwrite_ok=True)
        return self

    def write(self,rows):
        if self.__sheet == None:
            print("please create sheet..")
            return
        i = 0
        for row in rows:
            print("write",row)
            self.__sheet.write(i,0,row[0])
            self.__sheet.write(i,1,row[1])
            self.__sheet.write(i,2,row[2])
            i += 1;
        return self

    def save(self):
        self.__workbook.save(self.file)
        return self
