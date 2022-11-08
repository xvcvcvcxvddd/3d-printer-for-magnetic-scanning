import time
import serial
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
from time import sleep


ser = serial.Serial(  # 下面这些参数根据情况修改
  port='COM14',# 串口
  baudrate=115200,# 波特率
  timeout=2
)
ser1 = serial.Serial(  # 下面这些参数根据情况修改
  port='COM10',# 串口
  baudrate=115200,# 波特率
  timeout=2,
)
sleep(2)
for t in range(10):
    cmd1="G1G91 Z5F2000 \r\n G1G91 X-50F2000" #1.5s
    cmd2="G1G91 X50Y-5Z-5F4000" #0.75s

    print(cmd1)

    ser.write(bytes(cmd1+"\r\n", encoding='utf-8'))
    ser.write(bytes(cmd2+"\r\n", encoding='utf-8'))

    #############
    data = ''
    f=open('D:/python/test.csv','a')

    for i in range(140):
        data = ser1.readline()
        data = data.decode("utf-8")
        f.writelines(str(t))
        f.writelines(",")
        f.writelines(str(i))
        f.writelines(",")
        f.writelines(str(data[:-1]))

        sleep(0.01)
    f.close()
    sleep(2)

ser.write(bytes("G1G90 X0Y0F4000"+"\r\n", encoding='utf-8'))