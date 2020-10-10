
import pandas as pd
from pandas import Series
import numpy as np
import openpyxl


class Excel:

    def __init__(self, config):
        self.config = config
    #写Excel
    def write_excel(self,exc,sheetName,row,col,indexs,column):
        y = len(col)
        x = len(row)
        excel_writer = pd.ExcelWriter(r"E:/testrun/sys.xlsx",engine='openpyxl')
        df = pd.DataFrame(row,col)

        df2 = df.stack()
        df3 = df2.unstack(0)
        df3.index = Series(indexs)
        df3.columns = Series(column)
        print(df3)
        book = openpyxl.load_workbook(excel_writer.path)
        excel_writer.book = book
        #writer = pd.ExcelWriter(exc)

        df3.to_excel(excel_writer = excel_writer,sheet_name =sheetName )
        excel_writer.close()
        #sheet1.write(1,3,'2006/12/12')
        #sheet1.write_merge(6,6,1,3,'未知')#合并行单元格
        #sheet1.write_merge(1,2,3,3,'打游戏')#合并列单元格
        #sheet1.write_merge(4,5,3,3,'打篮球')
        #writer.save()



if __name__ == "__main__":
    # Unit test
    t = Excel({})

    input("Press ENTER to continue")
    print("do some unittest")
    print("PASS")
