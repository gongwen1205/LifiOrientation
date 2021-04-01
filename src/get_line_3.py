import pytesseract
from pytesser3 import *
from PIL import Image, ImageEnhance, ImageFilter
import os
import fnmatch
import re, time

import urllib, random


def getGray(image_file):
    tmpls = []
    for w in range(0, image_file.size[0]):  # h
        for h in range(0, image_file.size[1]):  # w
            tmpls.append(image_file.getpixel((w,h)))

    return tmpls
def getAvg(ls):  # 获取平均灰度值
    return sum(ls) / len(ls)

files = os.listdir("D:/videodata95% 100HZ")  # 图片文件夹地址自行替换
Blength = []
Dlength = []
for file in files:
    image_file = Image.open("D:/videodata95% 100HZ/" + str(file))
    image_file = image_file.convert("L")
    Grayls = getGray(image_file)
    new_avg_grey=[]
    k=0
    for i in range(0,image_file.size[0]):
        temp=0
        for j in range(0, image_file.size[1]):
            temp+=Grayls[k];
            k=k+1
        temp=temp/image_file.size[1]
        new_avg_grey.append(temp)
        #print(new_avg_grey)
    #new_avg_avg_grey = getAvg(new_avg_grey)
    BDlist = []
    print(len(new_avg_grey))
    for i in range(0, len(new_avg_grey)-1):
        if(abs(100*(new_avg_grey[i+1]-new_avg_grey[i])/new_avg_grey[i])>1):
            print(100*(new_avg_grey[i+1]-new_avg_grey[i])/new_avg_grey[i])
            print(i)
        if (new_avg_grey[i] > 10.0):
            BDlist.append('B')
        else:
            BDlist.append('D')
    temp = 0
    for i in range(0, len(BDlist) - 1):
        if (BDlist[i + 1] != BDlist[i]):
            if(temp==0):
                temp=i
            else :
                print(BDlist[i] + "区的长度为" + str(i-temp))
                print("from"+str(temp)+"to"+str(i))
                if(BDlist[i]=='B'):
                    Blength.append(i-temp)
                else:
                    Dlength.append(i-temp)
                temp=i
            #print(i)
            #print(BDlist[i] + "to" + BDlist[i + 1])
    print(str(file)+"one loop finish!")
B_avg=getAvg(Blength)
D_avg=getAvg(Dlength)
B_error=[]
D_error=[]
B_maxerror=0
D_maxerror=0
for i in range(len(Blength)):
    B_error.append(100*abs(Blength[i]-B_avg)/B_avg)
    if((100*abs(Blength[i]-B_avg)/B_avg)>B_maxerror):
        B_maxerror=100*abs(Blength[i]-B_avg)/B_avg
print(B_maxerror)
print(getAvg(B_error))
print("B finish!")
for j in range(len(Dlength)):
    D_error.append(100 * abs(Dlength[j] - D_avg) / D_avg)
    if ((100 * abs(Dlength[j] - D_avg) / D_avg) > D_maxerror):
        D_maxerror = 100 * abs(Dlength[j] - D_avg) / D_avg
print(D_maxerror)
print(getAvg(D_error))
print("D finish!")