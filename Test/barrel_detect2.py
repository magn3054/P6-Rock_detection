import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv.imread('C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Test/field_with_barrel.png')
img_rgb = cv.resize(img_rgb, (1014, 570), interpolation=cv.INTER_CUBIC)

img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Test/blue_barrel.png',0)

w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res <= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imshow('res', res)
cv.imshow('img_rgb', img_rgb)
cv.imshow('template', template)
cv.imshow('img_gray', img_gray)

cv.waitKey(0)
cv.destroyAllWindows()
