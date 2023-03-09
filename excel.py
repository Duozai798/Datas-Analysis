# -*- coding: utf-8 -*-
# @Time : 2023/3/7 20:04
# @Author : Ding Jun Ming
import xlrd
import xlwt
from xpinyin import Pinyin

def pinyin_tran(path,sheet,col):                                      # 参数:excel文件路径,表名,列值
    # 读取excel文件数据
    file = xlrd.open_workbook(path)
    table = file.sheet_by_name(sheet)
    ncols = table.ncols                                               # 获取原始表列数

    data = table.col_values(col-1, start_rowx=0, end_rowx=None)       # 获取需要转换拼音的列的数据

    # 将读取的数据转换为拼音
    pinyin = Pinyin()
    res = []
    for i in data:
        if type(i) != str:
            res.append(i)
        else:
            a = pinyin.get_pinyin(i)
            a = a.split('-')
            en = a[0].capitalize() + ' ' + ''.join(a[1:]).capitalize()      # 去掉"-"
            en = ''.join([i.strip(' ') for i in en])                        # 删除空格
            en = en.lower()                                                 # 转换为小写
            en = en + '@dslyy.com'                                          # 添加邮箱后缀
            res.append(en)                                                  # 追加到新列表


    # 写入excel文件并保存
    wookbook = xlwt.Workbook('encoding = utf-8')                             # 创建excel文件
    sheet = wookbook.add_sheet('new_'+sheet,cell_overwrite_ok=True)          # 创建new_sheet工作表
    for i in range(len(res)):
        sheet.write(i, ncols, res[i])                                        # 将转换后的数据写入新表
    wookbook.save(r"new.xlsx")

# test push
