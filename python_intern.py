import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial("COM2", 9600)
#print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

a=[]
str1=str(ser.readline())
print(str1)
a=str1.split(",")
a_x=a[0]
a_x=a_x[8:]
a_y=a[1]
a_y=a_y[6:]
a_z=a[2]
a_z=a_z[7:]
g_x=a[3]
g_x=g_x[8:]
g_y=a[4]
g_y=g_y[8:]
g_z=a[5]
g_z=g_z[8:][:-7]
print(a_z)
while res:
     cc=str(1234)
     print(cc)
     val=cc
     firebase1 = firebase.FirebaseApplication('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/', None)##paste your firebase url
     
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':a_x,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/'+ '/a_x_data/'+ str(i), data)##paste your firebase url
             print(result)
             
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':a_y,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/'+ '/a_y_data/'+ str(i), data)##paste your firebase url
             print(result)

     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':a_z,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/'+ '/a_z_data/'+ str(i), data)##paste your firebase url
             print(result)

      
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':g_x,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/'+ '/g_x_data/'+ str(i), data)##paste your firebase url
             print(result)
             
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':g_y,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/'+ '/g_y_data/'+ str(i), data)##paste your firebase url
             print(result)
             
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':g_z,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://iot-based-earhquake-prediction-default-rtdb.europe-west1.firebasedatabase.app/'+ '/g_z_data/'+ str(i), data)##paste your firebase url
             print(result)        

     res=0
