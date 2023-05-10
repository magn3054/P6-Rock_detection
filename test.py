import cv2


path = "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/"
try:
    with open(path) as f:
        print("The path exists!")
except FileNotFoundError:
    print("changing path")
    path = "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/"


path2 = f"{path}Images/26-04-2023/RGB_13;44;35.jpg"

img = cv2.imread(path2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows