
import pandas as pd
from pandas import Series
import openpyxl
import re
from math import ceil
import numpy as np

#---------------------S2.1.1----------------------------
passOrFail = []
columns =['vcc = 3.3','vcc = 5.0','vcc = 2.2']
index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0
chipnum = 0

with open("S2.1.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchchip = re.match( r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            chipnum = int(chip[1])
        searchObj = re.match( r'(.*?) vol is (.*).*', data, re.M|re.I|re.S)
        if searchObj:
            a=searchObj.groups(0)
            print(a[1])
            if a[0][-11:] == 'VCC is 3.3v':
                index = index +['core %d vbgs vol is' %chipnum]
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


excel_writer = pd.ExcelWriter("E:/testrun/sys.xlsx")
sheetName = 'S2.1.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
#excel_writer.close()



#---------------------S2.1.3----------------------------
index = []
fiv = []
thrv = []
twov = []
fivv = []
thrvv = []
twovv = []
vol = []
counter = 0

columns =['vcc = 3.3 fre', 'vcc = 3.3 dut','vcc = 5.0 fre','vcc = 5.0 dut','vcc = 2.2 fre','vcc = 2.2 dut']
with open("S2.1.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): VCC is (.*?) fre is (.*), duty is (.*).*', data, re.M|re.I|re.S)#"VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == '3.3v':
                index = index +[' core %d HRC fre and duty are' %counter]
                counter = counter +1
                thrv.append(a[2])
                thrvv.append(a[3])
            elif a[1] == '5v':
                fiv.append(a[2])
                fivv.append(a[3])
            elif a[1] == '2.2v':
                twov.append(a[2])
                twovv.append(a[3])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,thrvv,fiv,fivv,twov,twovv])
v = v.T
print(v)
v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.1.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)


#---------------------S2.1.4----------------------------
index = []
fiv = []
thrv = []
twov = []
fivv = []
thrvv = []
twovv = []
vol = []
counter = 0

columns =['vcc = 3.3 fre', 'vcc = 3.3 dut','vcc = 5.0 fre','vcc = 5.0 dut','vcc = 2.2 fre','vcc = 2.2 dut']
with open("S2.1.4.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): VCC is (.*?) fre is (.*), duty is (.*).*', data, re.M|re.I|re.S)#"VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == '3.3v':
                index = index +['core %d LRC fre and duty are' %counter]
                counter = counter +1
                thrv.append(a[2])
                thrvv.append(a[3])
            elif a[1] == '5v':
                fiv.append(a[2])
                fivv.append(a[3])
            elif a[1] == '2.2v':
                twov.append(a[2])
                twovv.append(a[3])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,thrvv,fiv,fivv,twov,twovv])
v = v.T
print(v)
v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.1.4'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)


#---------------------S2.1.5----------------------------
index = []
fiv = []
thrv = []
twov = []
fivv = []
thrvv = []
twovv = []
vol = []
counter = 0

columns =['vcc = 3.3 fre', 'vcc = 3.3 dut','vcc = 5.0 fre','vcc = 5.0 dut','vcc = 2.2 fre','vcc = 2.2 dut']
with open("S2.1.5.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): VCC is (.*?) fre is (.*), duty is (.*).*', data, re.M|re.I|re.S)#"VCC is 3.3v fre is %f, duty is %f" %(fre,duty))
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == '3.3v':
                index = index +['core %d MRC fre and duty are' %counter]
                counter = counter +1
                thrv.append(a[2])
                thrvv.append(a[3])
            elif a[1] == '5v':
                fiv.append(a[2])
                fivv.append(a[3])
            elif a[1] == '2.2v':
                twov.append(a[2])
                twovv.append(a[3])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,thrvv,fiv,fivv,twov,twovv])
v = v.T
print(v)
v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.1.5'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)


#---------------------S2.1.6----------------------------
index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0
j=-1
count = 0
mv = []
dic = {'0':"1200",'1':"1500",'2':"2000",'3':"2500"}

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']


with open("S2.1.6.txt", "r") as f:
    data = f.readline()
    if data[32:38] == 'ready:':
        mv = data[-8:]
    while data:
        print(data)
        searchObj = re.match(r'(.*?): VCC is (.*?) avg is (.*).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            print(a[1])
            if a[1] == '3.3v':
                #index = index +['core %d vref vol is under %s' %(counter/4,dic[str(int((i-1)/5))])]
                counter = counter +1
                thrv.append(a[2])
            elif a[1] == '5v':
                fivv.append(a[2])
            elif a[1] == '2.2v':
                twov.append(a[2])
        else:
            print("fail")
        data = f.readline()
        print(data[32:38])
        if data[32:38] == 'ready:':
            mv = data[-8:]

    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
print(v.shape)
pd3 =pd.DataFrame()

for j in range(0,int((len(v)-1)/4)):
    for i in range(0,ceil(len(v)/4)):
        if i*4+j>len(v)-1:
            break
        else:
            pd3 = pd3.append(v.loc[i*4+j].T)
j=-1
pd3.columns =  Series(columns)
count = (int(len(pd3))/4)
for i in range(0,len(pd3)):
    if i % count ==0.0:
        j = j + 1
    index = index +['core %d vref vol is under %s' %(j,dic[str(j)])]
pd3.index =  Series(index)
sheetName = 'S2.1.6'
pd3.to_excel(excel_writer = excel_writer,sheet_name =sheetName)

#---------------------S2.2.1----------------------------

index = []
fi = []
th = []
tw = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0
chipnum = []

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S2.2.1.txt", "r") as f:
    data = f.readline()
    if data[-10:-4] == 'V1P5S ':
        mv = data[-4:]


    while data:
        searchchip = re.match(r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            chipnum.append(int(chip[1]))

        searchObj = re.match(r'(.*?): VCC is (.*?) vol is (.*)', data, re.M|re.I|re.S)
        if searchObj:
            a=searchObj.groups(0)
            if a[1] == '3.3v':
                thrv.append(float(a[2]))
            elif a[1] == '5v':
                fivv.append(float(a[2]))
            elif a[1] == '2.2v':
                twov.append(float(a[2]))
        else:
            print("fail")
        data = f.readline()
        if data[-11:-5] == 'V1P5S ':
            mv = data[-5:]

    f.close()

    l = 0
    h = len(thrv)
    for i in range(0,len(thrv),2):
        th.append(thrv[i])
    for i in range(1,len(thrv),2):
        th.append(thrv[i])

    for i in range(0,len(fivv),2):
        fi.append(fivv[i])
    for i in range(1,len(fivv),2):
        fi.append(fivv[i])

    for i in range(0,len(twov),2):
        tw.append(twov[i])
    for i in range(1,len(twov),2):
        tw.append(twov[i])



v = pd.DataFrame([th,fi,tw])
v = v.T
pd3 =pd.DataFrame(v)




chipnum = chipnum+chipnum

for i in range(0,int(len(v))):
    if i<= int(len(v)/2):
	    index = index +['core %d V1P5S vol is under 1.5v' %chipnum[i]]
    if i> int(len(v)/2):
	    index = index +['core %d V1P5S vol is under 1.2v' %chipnum[i]]
pd3.columns =  Series(columns)
pd3.index =  Series(index)


sheetName = 'S2.2.1'
pd3.to_excel(excel_writer = excel_writer,sheet_name =sheetName)

#---------------------S2.2.3----------------------------

index = []
fivv = []
thrv = []
twov = []
vol = []
V1P5S_L = []
counter = 0

with open("S2.2.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): V1P5S_L vol is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            V1P5S_L.append(a[1])
            counter = counter +1
            vol = vol+['core %d vol is' %counter]
        data = f.readline()
    f.close()

v = pd.DataFrame(V1P5S_L)
v.index =  Series(vol)
v.columns =  Series(["V1P5S_L"])
sheetName = 'S2.2.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
V1P5S_L = []



#---------------------S2.2.4----------------------------
index = []
fi = []
th = []
tw = []
fiv = []
thrv = []
twov = []
fivv = []
thrvv = []
twovv = []
vol = []
counter = 0
chipnum = []

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S2.2.4.txt", "r") as f:
    data = f.readline()

    while data:
        searchchip = re.match(r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            chipnum.append(int(chip[1]))

        searchObj = re.match(r'(.*?): VCC is (.*?) vol is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            print(a[1])
            if a[1] == '3.3v':
                thrv.append(a[2])
            elif a[1] == '5v':
                fivv.append(a[2])
            elif a[1] == '2.2v':
                twov.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()
for i in range(0,len(thrv),2):
    th.append(thrv[i])
for i in range(1,len(thrv),2):
    th.append(thrv[i])

for i in range(0,len(fivv),2):
    fi.append(fivv[i])
for i in range(1,len(fivv),2):
    fi.append(fivv[i])

for i in range(0,len(twov),2):
    tw.append(twov[i])
for i in range(1,len(twov),2):
    tw.append(twov[i])
v = pd.DataFrame([th,fi,tw])
v = v.T
pd3 =pd.DataFrame(v)

chipnum = chipnum+chipnum

for i in range(0,int(len(v))):
    if i<= int(len(v)/2)-1:
	    index.append(['core %d V1P5D vol is under 1.5v' %chipnum[i]])
    if i> int(len(v)/2)-1:
	    index .append(['core %d V1P5D vol is under 1.2v' %chipnum[i]])

v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.2.4'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)

#---------------------S2.2.6----------------------------

index = []
fivv = []
thrv = []
twov = []
vol = []
V1P5D_L = []
counter = 0

with open("S2.2.6.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): V1P5D_L vol is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            V1P5D_L.append(a[1])
            counter =counter +1
            vol = vol+['core %d vol is' %counter]
        data = f.readline()
    f.close()

v = pd.DataFrame(V1P5D_L)
v.index =  Series(vol)
v.columns =  Series(["V1P5D_L"])
sheetName = 'S2.2.6'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
V1P5D_L = []


#---------------------S2.2.7----------------------------
index = []
fivv = []
thrv = []
twov = []
vol = []
fi = []
th = []
tw = []
chipnum = []
counter = 0
count = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
val = ['1.55','1.6','1.7','1.5','1.5 LOAD']
with open("S2.2.7.txt", "r") as f:
    data = f.readline()

    while data:
        searchchip = re.match(r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            chipnum.append(int(chip[1]))
        searchObj = re.match(r'(.*?): VCC is (.*?) vol is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            print(a[1])
            if a[1] == '3.3v':
                thrv.append(a[2])
            elif a[1] == '5v':
                fivv.append(a[2])
            elif a[1] == '2.2v':
                twov.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

for j in range(0,int(len(thrv)/len(chipnum))):
    for i in range (0+j,len(thrv),5):
        th.append(thrv[i])
for j in range(0,int(len(fivv)/len(chipnum))):
    for i in range (0+j,len(fivv),3):
        fi.append(fivv[i])
for j in range(0,int(len(twov)/len(chipnum))):
    for i in range (0+j,len(twov),3):
        tw.append(twov[i])



v = pd.DataFrame([th,fi,tw])
v = v.T
pd3 =pd.DataFrame(v)
temp =len(chipnum)
chipnum = chipnum*5

for i in range(0,int(len(v))):
    print(i)
    index = index +['core %d V1P5a vol is under %s' %(chipnum[int(i)],val[int(i/temp)])]

v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.2.7'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)


#---------------------S2.2.10----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
Visrch = []
counter = 0

with open("S2.2.10.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): Visrch vol is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            Visrch.append(a[1])
            counter =counter+1
            vol = vol+['core %d Visrch vol is' %counter]
        data = f.readline()
    f.close()

v = pd.DataFrame(Visrch)
v.columns =  Series(['vol'])
v.index =  Series(vol)
sheetName = 'S2.2.10'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
Visrch = []

#---------------------S2.2.11----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
Visrca = []
counter = 0

with open("S2.2.11.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): Visrca vol is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            Visrca.append(a[1])
            counter =counter+1
            vol = vol+['core %d Visrca vol is' %counter]
        data = f.readline()
    f.close()

v = pd.DataFrame(Visrca)
v.columns =  Series(['vol'])
v.index =  Series(vol)
sheetName = 'S2.2.11'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
Visrch = []


#---------------------S2.3----------------------------
index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S2.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): ISRCS amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            print(a)
            if a[2] == '3.3v\n':
                index = index +['core %d ISRCS vol is' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v\n':
                fivv.append(a[1])
            elif a[2] == '2.2v\n':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T

v.columns =  Series(columns)
v.index =  Series(index)


sheetName = 'S2.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)

#---------------------S2.4.1----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
datas = []
dat = []
chipnum = []
temp = 0

VOL = ['0mv','12mv','25mv','50mv',]


with open("S2.4.1.txt", "r") as f:
    data = f.readline()
    while data:
        searchchip = re.match(r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            chipnum.append(int(chip[1]))
        searchObj = re.match(r'(.*?): vol diff is (.*) mv.*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            datas.append(a[1])

        data = f.readline()
    f.close()
for j in range(0,int(len(datas)/len(chipnum))):
    for i in range (0+j,len(datas),4):
        dat.append(datas[i])


v = pd.DataFrame(dat)
temp = len(chipnum)
chipnum = chipnum*4
for i in range(0,int(len(v))):
    index = index +['core %d V1P5a vol is under %s' %(chipnum[int(i)],VOL[int(i/temp)])]

v.columns =  Series(["vol"])
v.index =  Series(index)
sheetName = 'S2.4.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []


#---------------------S2.4.2----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
cmp = []
counter = 0

with open("S2.4.2.txt", "r") as f:
    data = f.readline()
    while data:
        print(data[31:34])
        if data[31:34] == 'pass':
            passOrFail.append('pass')
        else :
            passOrFail.append('fail')
        data = f.readline()
    f.close()

#---------------------S2.5----------------------------


index = []
ind = []
vol = []
lvd = []
chipnum = []
num = []
counter = 0
count = 0
lv = []
testCond = ['检测vcc(低功耗) 2.5v','检测vcc 2.5v','检测外部电路LVDI0 2.5','检测外部电路LVDI1 2.5']#,'检测外部电路LVDI0 1.2-4.3']
nb = ''

with open("S2.5.txt", "r") as f:
    data = f.readline()
    while data:
        searchchip = re.match(r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            chipnum.append(int(chip[1]))
        search = re.match(r'(.*?) Right now is (.*).*', data, re.M|re.I|re.S)
        if search:
            chip=search.groups(0)
            num.append(int(chip[1][:-3])-200)
        searchObj = re.match(r'(.*?): final result is (.*).*', data, re.M|re.I|re.S)
        if searchObj:
            a=searchObj.groups(0)
            lvd.append(a[1])
        data = f.readline()
    f.close()

leng = len(chipnum)
for i in range(0,leng):
    nb += str(chipnum[i])*20
for i in range(0,leng*20):
    if 0 <=i%20 < 4:
        index.append(testCond[i%20] + ' in core %s' %nb[i])
    else :
        index.append('1.2-4.3:'+ str(num[i])+' in core %s' %nb[i])

for j in range(0,int(len(lvd)/leng)):
    for i in range (0+j,len(lvd),20):
        lv.append(lvd[i])
for j in range(0,int(len(index)/leng)):
    for i in range (0+j,len(index),20):
        ind.append(index[i])

v = pd.DataFrame(lv)
v = v.T
v.index =  Series(["lvd"])
v.columns=  Series(ind)
v = v.T
sheetName = 'S2.5'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
lv = []



#---------------------S2.6.1----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S2.6.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?): indled amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v\n':
                index = index +['core %d indled amp is ' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v\n':
                fivv.append(a[1])
            elif a[2] == '2.2v\n':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v=v.T
v.columns =  Series(columns)
v.index =  Series(index)

sheetName = 'S2.6.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []

#---------------------S2.7.1----------------------------

index = []
vol = []
pdSensorOut = []
counter = 0
count = 0
pd1 = []
vo1 = []
vi2 = []
vo2 =[]
vo = []
column =[]
wave =['vo1', 'vi2','vo2','vo']
columns = []

with open("S2.7.1.txt", "r") as f:
    data = f.readline()
    while data:

        searchObj = re.match(r'(.*?): wave_max is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            pdSensorOut.append(a[1])
            count = count +1
            if count%4==1:
                vo1.append(a[1])
            if count%4==2:
                vi2.append(a[1])
            if count%4==3:
                vo2.append(a[1])
            if count%4==0:
                vo.append(a[1])
            if (count-1)%4==0:
                counter = counter +1
                column = column+['core %d waveform vol is' %counter]

        data = f.readline()
    f.close()

v = pd.DataFrame([vo1,vi2,vo2,vo])
v=v.T

v.index =  Series(column)
v.columns=  Series(wave)


sheetName = 'S2.7.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
pdSensorOut = []

#---------------------S2.7.2----------------------------
import math
index = []
vol = []
pdSensorOut = []
column = []
col =[]
wavemax = []
chipnum = []
vi2 = []
i2 = []
vo2=[]
o2=[]
A = []
db = []
db1 = []
k=-1
counter = 0
count = 0
val =0
wave =['db', 'vi2','vo2','A']
with open("S2.7.2.txt", "r") as f:
    data = f.readline()
    while data:
        searchchip = re.match(r'(.*?) chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            chip=searchchip.groups(0)
            val +=1
            for i in range (0,36):
                chipnum.append(int(chip[1]))

        searchObj = re.match(r'(.*?): wave_max is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            k = k+1

            if counter <= 31 and k%2==0:
                db.append(str(counter)+'db')
                counter = counter +1
            elif counter ==32 and k%2==0:
                db.append('5v')
                counter = counter +1
            elif counter ==33 and k%2==0:
                db.append('2.2v')
                counter = counter +1
            elif counter ==34 and k%2==0:
                db.append('5v_smal')
                counter = counter +1
            elif counter ==35 and k%2==0 :
                db.append('2.2v_smal')
                counter =0

            if count%2==0:
                vi2.append(float(a[1][:-1]))
            elif count%2==1:
                vo2.append(float(a[1][:-1]))
            print("chipnum is %d" %len(chipnum))
            if (count)%2==0 :
                print(count)
                column = column+['core %d waveform vol is' %chipnum[int((count)/2)]]
            count = count+1




        data = f.readline()
    f.close()

for j in range(0,int(len(vi2)/val)):
    for i in range (0+j,len(vi2),36):
        i2.append(vi2[i])

for j in range(0,int(len(vo2)/val)):
    for i in range (0+j,len(vo2),36):
        o2.append(vo2[i])

for j in range(0,int(len(column)/val)):
    for i in range (0+j,len(column),36):
        col.append(column[i])

for j in range(0,int(len(db)/val)):
    for i in range (0+j,len(db),36):
        db1.append(db[i])


for i in range(0,len(o2)):
    a = (float(o2[i])/float(i2[i]))
    A.append(math.log(a,10)*20)


v = pd.DataFrame([db1,i2,o2,A])
v=v.T
v.index =  Series(col)
v.columns=  Series(wave)
sheetName = 'S2.7.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
pdSensorOut = []

#---------------------S2.8.1----------------------------
chip = []
vre = ''
vref1 =''
vref2 = []
jdg = 0
chi = ''
data = ''
vol1 = '3.3v'
inl = []
dnl = []
vol= []
vref = []
resp = []
mv = []
count = 0
k=0
cloumn = ['vref','vcc','resp','powersup','inl','dnl']

with open("temp.txt", "r") as fi:
    vref1 = fi.readline()
    for i in range(0,2):
        searchvref = re.match(r'(.*) VCC is (.*) avg is (.*).*', vref1, re.M|re.I|re.S)
        if searchvref:
            c=searchvref.groups(0)
            vref2.append(float(c[2]))
        vref1 = fi.readline()



with open("S2.8.1.txt", "r") as f:
    data = f.readline()

    while data:
        jdg == 0
        searchmv = data[32:38]
        if searchmv =='2600mv':
            k=k+1
            if k%6 == 0:
                vol1 = '5v'
                vref1 = vref2[1]
            elif k%7 == 0:
                vol1 = '2.2v'
                vref1 = vref2[2]
            else:
                vol1 = '3.3v'
                vref1 = vref2[0]
        vref1 = vref2[0]
        searchchip = re.match(r'(.*?): chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            c=searchchip.groups(0)
            chi = (c[1])

        searchinl = re.match(r'(.*?): inl is (.*)', data, re.M|re.I|re.S)
        if searchinl:
            c=searchinl.groups(0)
            inl.append(float(c[1]))
            vref.append(vref1)
            mv.append(vol1)
            chip.append(chi)

        searchdnl = re.match(r'(.*?): dnl is (.*)', data, re.M|re.I|re.S)
        if searchdnl:
            c=searchdnl.groups(0)
            dnl.append(float(c[1]))
        searchvol = re.match(r'(.*?): vol apply (.*)', data, re.M|re.I|re.S)
        if searchvol:
            c=searchvol.groups(0)
            vol.append(float(c[1]))
        searchresp = re.match(r'(.*?): resp is (.*)', data, re.M|re.I|re.S)
        if searchresp:
            c=searchresp.groups(0)
            resp.append((c[1][:-2]))
        data = f.readline()
    f.close()

v = pd.DataFrame([vref,mv,resp,vol,inl,dnl])
v=v.T
v.columns = Series(cloumn)
print(len(chip))
v.index = Series(chip)
print(v)
sheetName = 'S2.8.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
excel_writer.save()









#---------------------S2.8.2----------------------------
chip = []
vre = ''
vref1 =''
vref2 = []
vref3 = []
jdg = 0
chi = ''
data = ''
vol1 = '3.3v'
inl = []
dnl = []
vol= []
vref = []
resp = []
mv = []
count = 0
k=0
cloumn = ['vref','resp','powersup','inl','dnl']

with open("temp.txt", "r") as fi:
    for i in range(0,12,3):
        vref3.append(fi.readline())
        fi.readline()
        fi.readline()

    for i in range(0,4):
        searchvref = re.match(r'(.*) VCC is (.*) avg is (.*).*', vref3[i], re.M|re.I|re.S)
        if searchvref:
            c=searchvref.groups(0)
            vref2.append(float(c[2]))


with open("S2.8.2.txt", "r") as f:
    data = f.readline()
    while data:
        jdg == 0
        searchmv = data[36:38]
        if searchmv =='mv':
            k=k+1
            vref1 = vref2[(k-1)%3]


        searchchip = re.match(r'(.*?): chip no: (.*).*', data, re.M|re.I|re.S)
        if searchchip:
            c=searchchip.groups(0)
            chi = (c[1])

        searchinl = re.match(r'(.*?): inl is (.*)', data, re.M|re.I|re.S)
        if searchinl:
            c=searchinl.groups(0)
            inl.append(float(c[1]))
            vref.append(vref1)
            chip.append(chi)
        searchdnl = re.match(r'(.*?): dnl is (.*)', data, re.M|re.I|re.S)
        if searchdnl:
            c=searchdnl.groups(0)
            dnl.append(float(c[1]))
        searchvol = re.match(r'(.*?): vol apply (.*)', data, re.M|re.I|re.S)
        if searchvol:
            c=searchvol.groups(0)
            vol.append(float(c[1]))
        searchresp = re.match(r'(.*?): resp is (.*)', data, re.M|re.I|re.S)
        if searchresp:
            c=searchresp.groups(0)
            resp.append((c[1][:-2]))
        data = f.readline()
    f.close()

v = pd.DataFrame([vref,resp,vol,inl,dnl])
v=v.T
v.columns = Series(cloumn)
print(len(chip))
v.index = Series(chip)
print(v)
sheetName = 'S2.8.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
excel_writer.save()
#---------------------S2.8.4----------------------------
with open("S2.8.4.txt", "r") as f:
    data = f.readline()
    while data:
        if data[31:34] == 'pass':
            passOrFail.append(['2.8.4 pass'])
        else :
            passOrFail.append(['2.8.4 fail'])
    data = f.readline()
    f.close()

#---------------------S3.1.1----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S3.1.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):I_VCC amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v':
                fivv.append(a[1])
            elif a[2] == '2.2v':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.1.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []

#---------------------S3.1.2----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S3.1.2.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):I_dsleep amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v':
                fivv.append(a[1])
            elif a[2] == '2.2v':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.1.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []


#---------------------S3.1.3----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S3.1.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):I_pwrdown amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v':
                fivv.append(a[1])
            elif a[2] == '2.2v':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.1.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []

#---------------------S3.1.4----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S3.1.4.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):I_BVS amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                thrv.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.1.4'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)


#---------------------S3.1.5----------------------------


index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S3.1.5.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):I_sleep amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v':
                fivv.append(a[1])
            elif a[2] == '2.2v':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.1.5'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []

#---------------------S3.2.1----------------------------

index = []
osc1g = []
osc1l = []
vol = []
counter = 0

columns =['vcc up = 2.11', 'vcc down = 1.94']
with open("S3.2.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):osc1 data is (.*?) when osc2 (.*) than 1.5', data, re.M|re.I|re.S)#'osc1 data is %f when osc2 greater than 1.5'
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == 'greater':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                osc1g.append(a[1])
            elif a[2] == 'less':
                osc1l.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([osc1g,osc1l])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.2.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []


index = []
osc1g = []
osc1l = []
vol = []
counter = 0

#---------------------S3.2.2----------------------------

index = []
hur = []
slo = []
vol = []
counter = 0

columns =[' hurry up = 700', ' slow down = 100']
with open("S3.2.2.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) time is (.*) than 1.5', data, re.M|re.I|re.S)#'osc1 data is %f when osc2 greater than 1.5'
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == 'hurry up':
                index = index +['core %d vol is' %counter]
                counter = counter +1
                hur.append(a[2])
            elif a[1] == 'slow down':
                hur.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([hur,slo])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.2.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []


index = []
osc1g = []
osc1l = []
vol = []
counter = 0

#---------------------S3.3.1----------------------------
index = []
fivv = []
thrv = []
twov = []
vol = []
counter = 0

columns =['vcc = 3.3', 'vcc = 5.0','vcc = 2.2']
with open("S3.3.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):thermdrv amp is (.*?) when VCC is (.*)', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[2] == '3.3v':
                index = index +['core %d ' %counter]
                counter = counter +1
                thrv.append(a[1])
            elif a[2] == '5v':
                fivv.append(a[1])
            elif a[2] == '2.2v':
                twov.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([thrv,fivv,twov])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.3.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []

#---------------------S3.3.2----------------------------
index = []
I_BZNS = []
I_BZPB = []
I_BZPS = []
I_BZNB = []
vol = []
counter = 0

columns =['BZNS src = 0.5', 'BZPB src = 10','BZPS src = 0.5', 'BZNB src = 10']
with open("S3.3.2.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) amp is (.*?) when sourmeter is (.*)', data, re.M|re.I|re.S)
        if searchObj:
            a=searchObj.groups(0)

            print(a[2])
            if a[1] == 'I_BZNS':
                index = index +['core %d' %counter]
                counter = counter +1
                I_BZNS.append(a[2])
            elif a[1] == 'I_BZPB':
                I_BZNS10.append(a[2])
            elif a[1] == 'I_BZPS':
                I_BZPS.append(a[2])
            elif a[1] == 'I_BZNB':
                I_BZNB.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([I_BZNS,I_BZPB,I_BZPS,I_BZNB])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.3.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
#---------------------S3.3.3----------------------------
index = []
Ibled = []
Irbled = []
vol = []
counter = 0

columns =['Ibled','Irbled']
with open("S3.3.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) amp is (.*?) when VCC is 3.3v.*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == 'Ibled':
                index = index +['core %d ' %counter]
                counter = counter +1
                Ibled.append(a[1])
            elif a[1] == 'Irbled':
                Irbled.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([Ibled,Irbled])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.3.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []


#---------------------S3.4.1----------------------------

index = []
HORNS_d = []
HORNS_f = []
HORNB_d = []
HORNB_f = []
vol = []
counter = 0

columns =['HORNS','HORNB']
with open("S3.4.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) duty is (.*?) fre is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)

            print(a[1])
            if a[1] == 'channel1':
                index = index +['core %d ' %counter]
                counter = counter +1
                HORNS_d.append("HORNS_d is "+a[2])
                HORNS_f.append("HORNS_f is "+a[3])
            elif a[1] == 'channel2':
                HORNB_d.append("HORNB_d is "+a[2])
                HORNB_d.append("HORNB_f is "+a[3])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([[HORNS_d,HORNS_f],[HORNB_d,HORNB_f]])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S3.4.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
#---------------------S4.1.1----------------------------

with open("S4.1.1.txt", "r") as f:
    data = f.readline()
    count = 0
    while data:
        if data == 'pass':
            if count == 0:
                passOrFail.append(['case 4.1.1 pass'])
                count =count +1
            else:
                passOrFail.append(['pass'])
        else :
            if count == 0:
                passOrFail.append(['case 4.1.1 fail'])
                count =count +1
            else:
                passOrFail.append(['fail'])
    data = f.readline()
    f.close()

#---------------------S4.2.1----------------------------

with open("S4.2.1.txt", "r") as f:
    data = f.readline()
    count = 0
    while data:
        if data == 'case 4.2.1 pass':
            passOrFail.append(data)
        elif data == 'case 4.2.1 fail':
            passOrFail.append(data)

    data = f.readline()
    f.close()

#---------------------S5.1----------------------------
with open("S5.1.txt", "r") as f:
    data = f.readline()
    count = 0
    while data:
        if data == 'pass':
            if count == 0:
                passOrFail.append(['case 5.1 pass'])
                count =count +1
            else:
                passOrFail.append(['pass'])
        else :
            if count == 0:
                passOrFail.append(['case 5.1 fail'])
                count =count +1
            else:
                passOrFail.append(['fail'])
    data = f.readline()
    f.close()


#---------------------S6.1.1----------------------------

index = []
duty = []
fre = []
vol = []
counter = 0

columns =['duty','fre']
with open("S6.1.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):duty is (.*?), fre is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            index = index +['core %d ' %counter]
            counter = counter +1
            duty.append(a[1])
            fre.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame(['duty','fre'])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S6.1.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []

index = []
duty = []
fre = []
vol = []


#---------------------S6.2----------------------------

index = []
vol = []
counter = 0

columns =[]
with open("S6.2.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?)vol is (.*?) v.*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            if a[1][:3] == "vok":
                columns = columns+a[1]
                index = index +['core %d ' %counter]
                counter = counter +1
                vol.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame(vol)
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S6.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
index = []
vol = []

#---------------------S6.3----------------------------

index = []
vol = []
ipk = []
counter = 0

columns =['ipk']
with open("S6.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):ipk vol is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            index = index +['core %d ' %counter]
            counter = counter +1
            ipk.append(a[1])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame(ipk)
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S6.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
index = []
ipk = []

#---------------------S7.1----------------------------

index = []
vpp = []
vh = []
Tset = []
counter = 0

columns =['vpp','vh','Tset']
with open("S7.1.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            if a[1] == 'Tset':
                Tset.append(a[2])
                index = index +['core %d ' %counter]
                counter = counter +1
            elif a[1] == 'VPP':
                vpp.append(a[2])
            elif a[1] == 'VH':
                vh.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([vpp,vh,Tset])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S7.1'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
index = []
ipk = []

#---------------------S7.2----------------------------

index = []
vpp = []
vh = []
Tset = []
counter = 0

columns =['vpp','vh','Tset']
with open("S7.2.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            if a[1] == 'Tset':
                Tset.append(a[2])
                index = index +['core %d ' %counter]
                counter = counter +1
            elif a[1] == 'VPP':
                vpp.append(a[2])
            elif a[1] == 'VH':
                vh.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([vpp,vh,Tset])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S7.2'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
index = []
ipk = []

#---------------------S7.3----------------------------
index = []
vh = []
counter = 0

#VH output voltage pass
columns =['vh']
with open("S7.3.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):VH output voltage (.*?)(.*?).*', data, re.M|re.I|re.S)

        if searchObj:
            a=searchObj.groups(0)
            if a[1] == "pass":
                vh.append('pass'+a[2])
            elif a[1] == "passes" or a[1] == "fail":
                vh.append('pass'+a[2])
                index = index +['core %d ' %counter]
                counter = counter +1
            elif a[1] == "failed":
                vh.append('failed'+a[2])
        else:
            print(fail)
        data = f.readline()
    f.close()
v = pd.DataFrame([vpp,vh,Tset])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S7.3'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
index = []
vh = []
counter = 0

#---------------------S7.4----------------------------
index = []
vpp = []
vh = []
Tset = []
counter = 0

columns =['vpp','vh','Tset']
with open("S7.4.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            if a[1] == 'Tset':
                Tset.append(a[2])
                index = index +['core %d ' %counter]
                counter = counter +1
            elif a[1] == 'VPP':
                vpp.append(a[2])
            elif a[1] == 'VH':
                vh.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([vpp,vh,Tset])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S7.4'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
index = []
#---------------------S7.5----------------------------

index = []
vh = []
Tset = []
counter = 0

columns =['vh','Tset']
with open("S7.5.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):(.*?) is (.*?).*', data, re.M|re.I|re.S)#""VCC is 5v avg is %s" %(avg)
        if searchObj:
            a=searchObj.groups(0)
            if a[1] == 'time_intv':
                Tset.append(a[2])
                index = index +['core %d ' %counter]
                counter = counter +1
            elif a[1] == 'VH':
                vh.append(a[2])
        else:
            print("fail")
        data = f.readline()
    f.close()

v = pd.DataFrame([vh,Tset])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S7.5'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
cmp = []
index = []


#---------------------S7.6----------------------------

index = []
vh = []
Tset = []
counter = 0

columns =['vh']
with open("S7.6.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        searchObj = re.match(r'(.*?):VH output voltage (.*?)(.*?).*', data, re.M|re.I|re.S)

        if searchObj:
            a=searchObj.groups(0)
            if a[1] == "pass":
                vh.append('pass'+a[2])
            elif a[1] == "passes" or a[1] == "failed":
                vh.append('pass'+a[2])
                index = index +['core %d ' %counter]
                counter = counter +1
            elif a[1] == "fail":
                vh.append('failed'+a[2])
        else:
            print('fail')
        data = f.readline()
    f.close()
v = pd.DataFrame([vpp,vh,Tset])
v = v.T
v.columns =  Series(columns)
v.index =  Series(index)
sheetName = 'S7.6'
v.to_excel(excel_writer = excel_writer,sheet_name =sheetName)
index = []
vh = []
counter = 0


#---------------------S7.6----------------------------
excel_writer.save()
