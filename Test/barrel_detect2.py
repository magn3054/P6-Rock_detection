import cv2 as cv
from matplotlib.pyplot import title
import numpy as np

image_width = 1014
image_height = 570

kernel = np.ones((5,5),np.uint8)

cam1 = cv.imread("Test/field_with_barrel2.png")
cam1 = cv.resize(cam1, (image_width,image_height)) #(2028,1141) (1014,570)

hsv1 = cv.cvtColor(cam1, cv.COLOR_BGR2HSV)


## lower bound and upper bound for barrel color 
lower_monster = np.array([31, 158, 162])  
upper_monster = np.array([119, 255, 255])


## find the colors within the boundaries on image 
mask_monster1 = cv.inRange(hsv1, lower_monster, upper_monster)


## Remove unnecessary noise from masks 
mask_monster1 = cv.morphologyEx(mask_monster1, cv.MORPH_CLOSE, kernel)
mask_monster1 = cv.morphologyEx(mask_monster1, cv.MORPH_OPEN, kernel)


## Find contours from the mask 
contours_monster1, hierarchy = cv.findContours(mask_monster1.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#contours_monster1 = sorted(contours_monster1, key=lambda c: cv.contourArea(c), reverse=True) # Shows only the biggest bounding box
for cnt in contours_monster1:#[:1]:
    x, y, w, h = cv.boundingRect(cnt)
    area = cv.contourArea(cnt)
    bound_ratio = w/h
    print("Barrel " + str(w/h))
    print("area " + str(area))
    font = ((area**(1/2))**(1/2))/10
    print("Height " + str(h))
    if bound_ratio < 10:
        # cv.drawContours(cam1, cnt, -1, (255, 0, 255), 7)
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt,0.02 * peri, True)
        x, y, w, h = cv.boundingRect(approx)
        cv.rectangle(cam1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(cam1, "Barrel", (x, y -15), cv.FONT_HERSHEY_COMPLEX, font,
                    (0,0,255), 1)

## Showing the output
cv.imshow("Output", cam1)

cv.waitKey(0) 
cv.destroyAllWindows()