# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from py_utils.excel.excel_passer import Passer


def seek_row():
    rows = Passer("/ICESX/workSpaceBjrdc/company/assessment/2020/年度/result-1.xls").seek_sheet(0).rows()
    for row in rows:
        print(row[0].value, row[1].value)


def list_row():
    row = Passer("/ICESX/workSpaceBjrdc/company/assessment/2020/年度/result-1.xls").seek_sheet(0).seek_row(1).row()
    print("xx", row)


if __name__ == '__main__':
    seek_row()
    list_row()
