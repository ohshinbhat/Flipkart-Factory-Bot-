import cv2
import numpy as np
import serial
import time
from pyzbar.pyzbar import decode

arduinoData = serial.Serial('com6', 115200)
arduinoData.timeout = 1

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

a = ['I1', 'I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
B1 = set(a)

b = ['A9', 'I1', 'I2', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
B2 = set(b)

c = ['A9', 'I1', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
B3 = set(c)

d = ['A9', 'I2', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
B4 = set(d)

e = ['I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
B5 = set(e)

f = ['A10', 'I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J11', 'J19', 'J20']
B6 = set(f)

g = ['A10', 'I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J10', 'J11', 'J19', 'J20']
B7 = set(g)

h = ['A10', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J11', 'J19', 'J20']
B8 = set(h)

i = ['I2', 'I9', 'I12', 'I19', 'I20', 'J2','J10', 'J11', 'J19', 'J20']
B9 = set(i)

j = ['A11', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2','J10', 'J19', 'J20']
B10 = set(j)

k = ['A11', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J11', 'J20']
B11 = set(k)

l = ['A11', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J19']
B12 = set(l)

m = ['I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J11', 'J19']
B13 = set(m)

n = ['A12', 'I2', 'I9', 'I19', 'I20', 'J2', 'J10', 'J11', 'J19']
B14 = set(n)

o = ['A12', 'I2', 'I9', 'I12', 'I20', 'J2', 'J10', 'J11', 'J19']
B15 = set(o)

p = ['A12', 'I2', 'I9', 'I19', 'J2', 'J10', 'J11', 'J19']
B16 = set(p)

q = ['I2', 'I9', 'I12', 'I19', 'J2', 'J10', 'J11', 'J19']
S1 = set(q)

r = ['A9', 'I1', 'I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
F1 = set(r)

s = ['A9', 'I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
F2 = set(s)

t = ['A10', 'I2', 'I9', 'I12', 'I19', 'I20', 'J1', 'J2', 'J10', 'J11', 'J19', 'J20']
F3 = set(t)

u = ['A10', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J11', 'J19', 'J20']
F4 = set(u)

v = ['A11', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J11', 'J19', 'J20']
F5 = set(v)

w = ['A11', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J11', 'J19']
F6 = set(w)

x = ['A12', 'I2', 'I9', 'I12', 'I19', 'I20', 'J2', 'J10', 'J11', 'J19']
F7 = set(x)

y = ['A12', 'I2', 'I9', 'I12', 'I19', 'J2', 'J10', 'J11', 'J19']
F8 = set(y)


with open('Bot 1 start.txt') as f:
    myDataList1 = f.read().splitlines()
with open('Bot 1 turn right and move forward.txt') as f:
    myDataList2 = f.read().splitlines()
with open('Bot 1 flip drop, U-turn and move forward.txt') as f:
    myDataList3 = f.read().splitlines()
with open('Bot 1 turn left and move forward.txt') as f:
    myDataList4 = f.read().splitlines()
with open('Bot 2 start.txt') as f:
    myDataList5 = f.read().splitlines()
with open('Bot 2 turn right and move forward.txt') as f:
    myDataList6 = f.read().splitlines()
with open('Bot 2 flip drop, U-turn and move forward.txt') as f:
    myDataList7 = f.read().splitlines()
with open('Bot 2 turn left and move forward.txt') as f:
    myDataList8 = f.read().splitlines()
with open('Bot 3 start.txt') as f:
    myDataList9 = f.read().splitlines()
with open('Bot 3 turn left and move forward.txt') as f:
    myDataList10 = f.read().splitlines()
with open('Bot 3 flip drop, U-turn and move forward.txt') as f:
    myDataList11 = f.read().splitlines()
with open('Bot 3 turn right and move forward.txt') as f:
    myDataList12 = f.read().splitlines()
with open('Bot 4 start.txt') as f:
    myDataList13 = f.read().splitlines()
with open('Bot 4 turn left and move forward.txt') as f:
    myDataList14 = f.read().splitlines()
with open('Bot 4 flip drop, U-turn and move forward.txt') as f:
    myDataList15 = f.read().splitlines()
with open('Bot 4 turn right and move forward.txt') as f:
    myDataList16 = f.read().splitlines()
with open('BREAK.txt') as f:
    myDataList17 = f.read().splitlines()
with open('Bot 1 forward before delivery.txt') as f:
    myDataList18 = f.read().splitlines()
with open('Bot 1 move forward after delivery.txt') as f:
    myDataList19 = f.read().splitlines()
with open('Bot 2 move forward before delivery.txt') as f:
    myDataList20 = f.read().splitlines()
with open('Bot 2 move forward after delivery.txt') as f:
    myDataList21 = f.read().splitlines()
with open('Bot 3 move forward before delivery.txt') as f:
    myDataList22 = f.read().splitlines()
with open('Bot 3 move forward after delivery.txt') as f:
    myDataList23 = f.read().splitlines()
with open('Bot 4 move forward before delivery.txt') as f:
    myDataList24 = f.read().splitlines()
with open('Bot 4 move forward after delivery.txt') as f:
    myDataList25 = f.read().splitlines()


while True:
    myData1 = []
    myData2 = []
    myData3 = []
    myData4 = []
    myData5 = []
    myData6 = []
    myData7 = []
    myData8 = []
    myData9 = []
    myData10 = []
    myData11 = []
    myData12 = []
    myData13 = []
    myData14 = []
    myData15 = []
    myData16 = []
    myData17 = []
    myData18 = []
    myData19 = []
    myData20 = []
    myData21 = []
    myData22 = []
    myData23 = []
    myData24 = []
    myData25 = []
    myData26 = []
    myData27 = []
    myData28 = []
    myData29 = []
    myData30 = []
    myData31 = []
    myData32 = []
    myData33 = []
    success, img = cap.read()

    for barcode in decode(img):
        myData1.append(barcode.data.decode('utf-8'))
        Z1 = set(myData1)
        if Z1 == B1:
            # while True:
            print(myData1)
            print("Bot 1 start")
            i = '1'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData2.append(barcode.data.decode('utf-8'))
        Z2 = set(myData2)
        if Z2 == F1:
            # while True:
            print(myData2)
            print("Bot 1 forward before delivery")
            i = '1'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData3.append(barcode.data.decode('utf-8'))
        Z3 = set(myData3)
        if Z3 == B2:
            # while True:
            print(myData3)
            print("Bot 1 turn right and move forward")
            i = '2'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData4.append(barcode.data.decode('utf-8'))
        Z4 = set(myData4)
        if Z4 == F1:
            # while True:
            print(myData4)
            print("Bot 1 forward before delivery")
            i = '1'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData5.append(barcode.data.decode('utf-8'))
        Z5 = set(myData5)
        if Z5 == B3:
            # while True:
            print(myData5)
            print("Bot 1 flip drop, U-turn and move forward")
            i = '3'
            arduinoData.write(i.encode())
            time.sleep(0.5)
         # arduinoData.close()
         # break

    for barcode in decode(img):
         myData6.append(barcode.data.decode('utf-8'))
         Z6 = set(myData6)
         if Z6 == F2:
            # while True:
             print(myData6)
             print("Bot 1 forward after delivery")
             i = '1'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
        myData7.append(barcode.data.decode('utf-8'))
        Z7 = set(myData7)
        if Z7 == B4:
            # while True:
            print(myData7)
            print("Bot 1 turn left and move forward")
            i = '4'
            arduinoData.write(i.encode())
            time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
         myData8.append(barcode.data.decode('utf-8'))
         Z8 = set(myData8)
         if Z8 == F2:
            # while True:
             print(myData8)
             print("Bot 1 forward after delivery")
             i = '1'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break





    for barcode in decode(img):
        myData9.append(barcode.data.decode('utf-8'))
        Z9 = set(myData9)
        if Z9 == B5:
            # while True:
            print(myData9)
            print("Bot 2 start")
            i = '5'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData10.append(barcode.data.decode('utf-8'))
        Z10 = set(myData10)
        if Z10 == F3:
            # while True:
            print(myData10)
            print("Bot 2 forward before delivery")
            i = '5'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData11.append(barcode.data.decode('utf-8'))
        Z11 = set(myData11)
        if Z11 == B6:
            # while True:
            print(myData11)
            print("Bot 2 turn right and move forward")
            i = '6'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData12.append(barcode.data.decode('utf-8'))
        Z12 = set(myData12)
        if Z12 == F3:
            # while True:
            print(myData12)
            print("Bot 2 forward before delivery")
            i = '5'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData13.append(barcode.data.decode('utf-8'))
        Z13 = set(myData13)
        if Z13 == B7:
            # while True:
            print(myData13)
            print("Bot 2 flip drop, U-turn and move forward")
            i = '7'
            arduinoData.write(i.encode())
            time.sleep(0.5)
         # arduinoData.close()
         # break

    for barcode in decode(img):
         myData14.append(barcode.data.decode('utf-8'))
         Z14 = set(myData14)
         if Z14 == F4:
            # while True:
             print(myData14)
             print("Bot 2 forward after delivery")
             i = '5'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
        myData15.append(barcode.data.decode('utf-8'))
        Z15 = set(myData15)
        if Z15 == B8:
            # while True:
            print(myData15)
            print("Bot 2 turn left and move forward")
            i = '8'
            arduinoData.write(i.encode())
            time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
         myData16.append(barcode.data.decode('utf-8'))
         Z16 = set(myData16)
         if Z16 == F4:
            # while True:
             print(myData16)
             print("Bot 2 forward after delivery")
             i = '5'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break





    for barcode in decode(img):
        myData17.append(barcode.data.decode('utf-8'))
        Z17 = set(myData17)
        if Z17 == B9:
            # while True:
            print(myData17)
            print("Bot 3 start")
            i = '9'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData18.append(barcode.data.decode('utf-8'))
        Z18 = set(myData18)
        if Z18 == F5:
            # while True:
            print(myData18)
            print("Bot 3 forward before delivery")
            i = '9'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData19.append(barcode.data.decode('utf-8'))
        Z19 = set(myData19)
        if Z19 == B10:
            # while True:
            print(myData19)
            print("Bot 3 turn left and move forward")
            i = '10'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData20.append(barcode.data.decode('utf-8'))
        Z20 = set(myData20)
        if Z20 == F5:
            # while True:
            print(myData20)
            print("Bot 3 forward before delivery")
            i = '9'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData21.append(barcode.data.decode('utf-8'))
        Z21 = set(myData21)
        if Z21 == B11:
            # while True:
            print(myData21)
            print("Bot 3 flip drop, U-turn and move forward")
            i = '11'
            arduinoData.write(i.encode())
            time.sleep(0.5)
         # arduinoData.close()
         # break

    for barcode in decode(img):
         myData22.append(barcode.data.decode('utf-8'))
         Z22 = set(myData22)
         if Z22 == F6:
            # while True:
             print(myData22)
             print("Bot 3 forward after delivery")
             i = '9'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
        myData23.append(barcode.data.decode('utf-8'))
        Z23 = set(myData23)
        if Z23 == B12:
            # while True:
            print(myData23)
            print("Bot 3 turn right and move forward")
            i = '12'
            arduinoData.write(i.encode())
            time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
         myData24.append(barcode.data.decode('utf-8'))
         Z24 = set(myData24)
         if Z24 == F6:
            # while True:
             print(myData24)
             print("Bot 3 forward after delivery")
             i = '9'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break




    for barcode in decode(img):
        myData25.append(barcode.data.decode('utf-8'))
        Z25 = set(myData25)
        if Z25 == B13:
            # while True:
            print(myData25)
            print("Bot 4 start")
            i = '13'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData26.append(barcode.data.decode('utf-8'))
        Z26 = set(myData26)
        if Z26 == F7:
            # while True:
            print(myData26)
            print("Bot 4 forward before delivery")
            i = '13'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData27.append(barcode.data.decode('utf-8'))
        Z27 = set(myData27)
        if Z27 == B14:
            # while True:
            print(myData27)
            print("Bot 4 turn left and move forward")
            i = '14'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData28.append(barcode.data.decode('utf-8'))
        Z28 = set(myData28)
        if Z28 == F7:
            # while True:
            print(myData28)
            print("Bot 4 forward before delivery")
            i = '13'
            arduinoData.write(i.encode())
            time.sleep(0.5)
        # arduinoData.close()
        # break

    for barcode in decode(img):
        myData29.append(barcode.data.decode('utf-8'))
        Z29 = set(myData29)
        if Z29 == B15:
            # while True:
            print(myData29)
            print("Bot 4 flip drop, U-turn and move forward")
            i = '15'
            arduinoData.write(i.encode())
            time.sleep(0.5)
         # arduinoData.close()
         # break

    for barcode in decode(img):
         myData30.append(barcode.data.decode('utf-8'))
         Z30 = set(myData30)
         if Z30 == F8:
            # while True:
             print(myData30)
             print("Bot 4 forward after delivery")
             i = '13'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
        myData31.append(barcode.data.decode('utf-8'))
        Z31 = set(myData31)
        if Z31 == B16:
            # while True:
            print(myData23)
            print("Bot 4 turn right and move forward")
            i = '16'
            arduinoData.write(i.encode())
            time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
         myData32.append(barcode.data.decode('utf-8'))
         Z32 = set(myData32)
         if Z32 == F8:
            # while True:
             print(myData32)
             print("Bot 4 forward after delivery")
             i = '13'
             arduinoData.write(i.encode())
             time.sleep(0.5)
            # arduinoData.close()
            # break

    for barcode in decode(img):
         myData33.append(barcode.data.decode('utf-8'))
         Z33 = set(myData33)
         if Z33 == S1:
            # while True:
             print(myData33)
             print("BREAK")
             arduinoData.close()
             break

    else:
        print("Unauthorised")
        
    for barcode in decode(img):
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
    cv2.imshow('Result', img)
    cv2.waitKey(1)