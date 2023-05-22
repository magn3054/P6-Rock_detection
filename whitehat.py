# import the necessary packages
import cv2
img_path = "./Images/10-05-2023/RGB_09;32;22.jpg"
therm_path = "./Images/10-05-2023/Thermal_09;32;22.jpg"

# load the image and convert it to grayscale
imagew = cv2.imread(img_path)
grayw = cv2.cvtColor(imagew, cv2.COLOR_BGR2GRAY)
  
# construct a rectangular kernel and 
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  #(13, 5)
 
# a tophat (also called a "whitehat") operation will enable
# us to find light(bright) regions on a dark background
tophat = cv2.morphologyEx(grayw, cv2.MORPH_TOPHAT, rectKernel)

###
# load the image and convert it to grayscale
imagetw = cv2.imread(therm_path)
graytw = cv2.cvtColor(imagetw, cv2.COLOR_BGR2GRAY)
  
# construct a rectangular kernel and 
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
 
# a tophat (also called a "whitehat") operation will enable
# us to find light(bright) regions on a dark background
tophatt = cv2.morphologyEx(graytw, cv2.MORPH_TOPHAT, rectKernel)
 



# load the image and convert it to grayscale
imageb = cv2.imread(img_path)
grayb = cv2.cvtColor(imageb, cv2.COLOR_BGR2GRAY)
  
# construct a rectangular kernel and 
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
 
# apply a blackhat operation which enables us to find dark regions on a light background
blackhat = cv2.morphologyEx(grayb, cv2.MORPH_BLACKHAT, rectKernel)
 
####
# load the image and convert it to grayscale
imagetb = cv2.imread(therm_path)
graytb = cv2.cvtColor(imagetb, cv2.COLOR_BGR2GRAY)
  
# construct a rectangular kernel and 
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
 
# apply a blackhat operation which enables us to find dark regions on a light background
blackhatt = cv2.morphologyEx(graytb, cv2.MORPH_BLACKHAT, rectKernel)
 



# show the output images
cv2.imshow("Original white", imagew)
cv2.imshow("Tophat", tophat)
# show the output images
cv2.imshow("Originalblack", imageb)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
# show the output images
cv2.imshow("Original therm white", imagetw)
cv2.imshow("Tophat therm", tophatt)
# show the output images
cv2.imshow("Original therm black", imagetb)
cv2.imshow("Blackhat therm", blackhatt)
cv2.waitKey(0)
