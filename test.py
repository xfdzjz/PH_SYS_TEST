
import pandas as pd
from pandas import Series
import openpyxl
import re
columns =['vcc = 3.3','vcc = 5.0','vcc = 2.2']
index = []
fre = []
duty = []
vol = []
counter = 0
index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0






with open("S2.1.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match( r'(.*?) vol is (.*).*', data, re.M|re.I|re.S)
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[0][-11:] == 'VCC is 3.3v':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                thrv.append(a[1][:-1])
            elif a[0][-11:] == 'VCC is 5.0v':
                fivv.append(a[1][:-1])
            elif a[0][-11:] == 'VCC is 2.2v':
                twov.append(a[1][:-1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T

v.columns =  Series(columns)
v.index =  Series(index)


excel_writer = pd.ExcelWriter("G:/testrun/sys.xlsx")
sheetName = 'S2.1.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
#excel_writer.close()

#---------------------

index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S2.1.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): VCC is (.*?) fre is (.*), duty is (.*).*', data, re.M|re.I|re.S)#"VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == '3.3v':
                index = index +['core %d fre and duty are' %counter]
                counter = counter +1
                thrv.append([a[2],a[3]])
            elif a[1] == '5v':
                fivv.append([a[2],a[3]])
            elif a[1] == '2.2v':
                twov.append([a[2],a[3]])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
print(v)
v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.1.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
excel_writer.save()