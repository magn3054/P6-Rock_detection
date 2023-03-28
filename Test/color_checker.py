import time
from turtle import color
import cv2
from cv2 import colorChange
from cv2 import WND_PROP_TOPMOST
from cv2 import setMouseCallback
import numpy as np
from tkinter import *
import tkinter as tkk
import tkinter.ttk
tk=tkk.Tk()

''' ## This is not included in the code yet ##
def next():
    tk.destroy()

tk.title("First")
tk.resizable(width=True, height=True)

tk.geometry('300x150')
tk.winfo_geometry

nb = tkinter.ttk.Notebook(tk, width=300, height=150)
nb.place(x=0, y=0)

pixelVirtual = tkk.PhotoImage(width=1, height=1) # gør at Button 'height' og 'width' gives i pixel #importerer et billede på 1 pixel

tekst = tkk.Label(tk, text ='Run ColorChecker?', font = ("Arial", 16, 'bold'), image=pixelVirtual, height=50, width=200, compound='c', bg='white')
tekst.place(x=50, y=10)

continue_button = Button(tk, borderwidth=3, text= "CONTINUE", font = ("Arial", 12, 'bold'), image=pixelVirtual, height=45, width=80, compound='c',  bg='green', fg='black', highlightbackground='#006600', activebackground= '#006600', command=tk.destroy) # , command=
continue_button.place(x=150-100, y=150/2)

#continue_button = Button(borderwidth=3, text= "Continue", font = ("Arial", 12, 'bold'), height=45, width=80,  bg='green', fg='black', highlightbackground='#006600', activebackground= '#006600', command=tk.destroy) # , command=
#continue_button.place(x=150-100, y=150/2)

tk.mainloop()
'''
sX = tk.winfo_screenwidth()
sY = tk.winfo_screenheight()
lenX = round(sX/3.025-5)

## 
frameWidth = 640
frameHeight = 480
cap = cv2.imread("Test/field_with_barrel.png")
cap = cv2.resize(cap, (1014,570)) #(2028,1141)

def stackImages(scale,imgArray): ## This def makes it so images can get displayed on a second row 
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver  

def empty(m):
    pass

## Sets the background color
bg = np.zeros((sY,sX,3), np.uint8)
bg[:]=(0,102,0)
cv2.namedWindow("background", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('background', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.resizeWindow("background", sX, sY)
cv2.imshow("background",bg)
##

cv2.namedWindow("MONSTER")
cv2.resizeWindow("MONSTER", lenX, 200)
cv2.createTrackbar("HUE Min", "MONSTER", 0,179, empty)  #normalt går HUE til 360, men i cv går den kun til 180  
cv2.createTrackbar("HUE Max", "MONSTER", 179,179, empty)
cv2.createTrackbar("SAT Min", "MONSTER", 0,255, empty) #SAT=saturation
cv2.createTrackbar("SAT Max", "MONSTER", 255,255, empty)
cv2.createTrackbar("VALUE Min", "MONSTER", 0,255, empty)
cv2.createTrackbar("VALUE Max", "MONSTER", 255,255, empty)

cv2.namedWindow("ZERO")
cv2.resizeWindow("ZERO", lenX, 200)
cv2.createTrackbar("HUE Min", "ZERO", 0,179, empty)  #normalt går HUE til 360, men i cv går den kun til 180  
cv2.createTrackbar("HUE Max", "ZERO", 179,179, empty)
cv2.createTrackbar("SAT Min", "ZERO", 0,255, empty) #SAT=saturation
cv2.createTrackbar("SAT Max", "ZERO", 255,255, empty)
cv2.createTrackbar("VALUE Min", "ZERO", 0,255, empty)
cv2.createTrackbar("VALUE Max", "ZERO", 255,255, empty)

cv2.namedWindow("JUICED")
cv2.resizeWindow("JUICED", lenX, 200)
cv2.createTrackbar("HUE Min", "JUICED", 0,179, empty)  #normalt går HUE til 360, men i cv går den kun til 180  
cv2.createTrackbar("HUE Max", "JUICED", 179,179, empty)
cv2.createTrackbar("SAT Min", "JUICED", 0,255, empty) #SAT=saturation
cv2.createTrackbar("SAT Max", "JUICED", 255,255, empty)
cv2.createTrackbar("VALUE Min", "JUICED", 0,255, empty)
cv2.createTrackbar("VALUE Max", "JUICED", 255,255, empty)

cv2.namedWindow("PUNCH")
cv2.resizeWindow("PUNCH", lenX, 200)
cv2.createTrackbar("HUE Min", "PUNCH", 0,179, empty)  #normalt går HUE til 360, men i cv går den kun til 180  
cv2.createTrackbar("HUE Max", "PUNCH", 179,179, empty)
cv2.createTrackbar("SAT Min", "PUNCH", 0,255, empty) #SAT=saturation
cv2.createTrackbar("SAT Max", "PUNCH", 255,255, empty)
cv2.createTrackbar("VALUE Min", "PUNCH", 0,255, empty)
cv2.createTrackbar("VALUE Max", "PUNCH", 255,255, empty)


while True:

## Monster color values
    h_monster_min = cv2.getTrackbarPos("HUE Min", "MONSTER") 
    h_monster_max = cv2.getTrackbarPos("HUE Max", "MONSTER")
    s_monster_min = cv2.getTrackbarPos("SAT Min", "MONSTER")
    s_monster_max = cv2.getTrackbarPos("SAT Max", "MONSTER")
    v_monster_min = cv2.getTrackbarPos("VALUE Min", "MONSTER")
    v_monster_max = cv2.getTrackbarPos("VALUE Max", "MONSTER")

## Zero color values
    h_zero_min = cv2.getTrackbarPos("HUE Min", "ZERO") 
    h_zero_max = cv2.getTrackbarPos("HUE Max", "ZERO")
    s_zero_min = cv2.getTrackbarPos("SAT Min", "ZERO")
    s_zero_max = cv2.getTrackbarPos("SAT Max", "ZERO")
    v_zero_min = cv2.getTrackbarPos("VALUE Min", "ZERO")
    v_zero_max = cv2.getTrackbarPos("VALUE Max", "ZERO")

## Juiced color values
    h_juiced_min = cv2.getTrackbarPos("HUE Min", "JUICED") 
    h_juiced_max = cv2.getTrackbarPos("HUE Max", "JUICED")
    s_juiced_min = cv2.getTrackbarPos("SAT Min", "JUICED")
    s_juiced_max = cv2.getTrackbarPos("SAT Max", "JUICED")
    v_juiced_min = cv2.getTrackbarPos("VALUE Min", "JUICED")
    v_juiced_max = cv2.getTrackbarPos("VALUE Max", "JUICED")

## Punch color values
    h_punch_min = cv2.getTrackbarPos("HUE Min", "PUNCH") 
    h_punch_max = cv2.getTrackbarPos("HUE Max", "PUNCH")
    s_punch_min = cv2.getTrackbarPos("SAT Min", "PUNCH")
    s_punch_max = cv2.getTrackbarPos("SAT Max", "PUNCH")
    v_punch_min = cv2.getTrackbarPos("VALUE Min", "PUNCH")
    v_punch_max = cv2.getTrackbarPos("VALUE Max", "PUNCH")

##

    img = cap
    #img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  ## Converts the image to HSV colorspace 

    lower_monster = np.array([h_monster_min, s_monster_min, v_monster_min]) ## Combines the lower values set from the trackbar and makes a tuple
    upper_monster = np.array([h_monster_max, s_monster_max, v_monster_max]) ## Combines the higher values set from the trackbar and makes a tuple
    mask_monster = cv2.inRange(imgHsv, lower_monster, upper_monster)        ## Gives values in the range of minimum and maximum and puts the on the HSV image as a "mask"
    result_monster = cv2.bitwise_and(img, img, mask = mask_monster)         ## Merges original image and the mask and outputs only what is present in both versions
    
    lower_zero = np.array([h_zero_min, s_zero_min, v_zero_min])
    upper_zero = np.array([h_zero_max, s_zero_max, v_zero_max])
    mask_zero = cv2.inRange(imgHsv, lower_zero, upper_zero)
    result_zero = cv2.bitwise_and(img, img, mask = mask_zero)

    lower_juiced = np.array([h_juiced_min, s_juiced_min, v_juiced_min])
    upper_juiced = np.array([h_juiced_max, s_juiced_max, v_juiced_max])
    mask_juiced = cv2.inRange(imgHsv, lower_juiced, upper_juiced)
    result_juiced = cv2.bitwise_and(img, img, mask = mask_juiced)

    lower_punch = np.array([h_punch_min, s_punch_min, v_punch_min])
    upper_punch = np.array([h_punch_max, s_punch_max, v_punch_max])
    mask_punch = cv2.inRange(imgHsv, lower_punch, upper_punch)
    result_punch = cv2.bitwise_and(img, img, mask = mask_punch)

    lower_zero = np.array([h_zero_min, s_zero_min, v_zero_min])
    upper_zero = np.array([h_zero_max, s_zero_max, v_zero_max])
    mask_zero = cv2.inRange(imgHsv, lower_zero, upper_zero)
    result_zero = cv2.bitwise_and(img, img, mask = mask_zero)


    cv2.rectangle(img, (85,5), (550,40), color=(0,0,0), thickness=-1)
    cv2.putText(img, text="press \'spacebar\' to continue", org=(90,30),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,255), thickness=2) #pos: x= Rect1+5, y= Rect1+25 

    cv2.rectangle(result_monster, (85,5), (490,40), color=(0,0,0), thickness=-1)
    cv2.putText(result_monster, text="Isolate color of 'Monster'", org=(90,30),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,255), thickness=2) #pos: x= Rect1+5, y= Rect1+25

    cv2.rectangle(result_zero, (115,5), (465,45), color=(0,0,0), thickness=-1)
    cv2.putText(result_zero, text="Isolate color of 'Zero'", org=(120,30),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,255), thickness=2) #pos: x= Rect1+5, y= Rect1+25
    
    cv2.rectangle(result_juiced, (85,5), (465,40), color=(0,0,0), thickness=-1)
    cv2.putText(result_juiced, text="Isolate color of 'Juiced'", org=(90,30),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,255), thickness=2) #pos: x= Rect1+5, y= Rect1+25

    cv2.rectangle(result_punch, (115,5), (495,40), color=(0,0,0), thickness=-1)
    cv2.putText(result_punch, text="Isolate color of 'Punch'", org=(120,30),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,255), thickness=2) #pos: x= Rect1+5, y= Rect1+25

    
    Stack = stackImages(0.8,([result_monster, result_zero], 
                            [result_juiced, result_punch]))
    
    cv2.namedWindow('Original image') 
    cv2.namedWindow('Color correction') 
    

    ## Window positions
    cv2.moveWindow('Original image', 0, 0)
    cv2.moveWindow('Color correction', lenX+15, 0)
    cv2.moveWindow("MONSTER", 0, round(sY-510))
    cv2.moveWindow("ZERO", 0, round(sY-255))
    cv2.moveWindow("JUICED", lenX+7, sY-255)
    cv2.moveWindow("PUNCH", lenX*2+5, sY-255) #round(sY-275)
    ##

    cv2.imshow('Original image', img)
    cv2.imshow('Color correction', Stack)

    
    if cv2.waitKey(1) & 0XFF == ord(' '):
        break





cap.release()
cv2.destroyAllWindows()
