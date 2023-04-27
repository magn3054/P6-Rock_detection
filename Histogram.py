import cv2
import numpy as np
import matplotlib.pyplot as plt


class ImageHistograms1:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path)

        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        self.hist = cv2.calcHist([self.gray], [0], None, [256], [0, 256])
        
    def plot_histograms(self):
        plt.figure(figsize=(10, 4))

        plt.subplot(131)
        plt.plot(self.hist)
        plt.title("Image")

        plt.show()




class ImageHistograms3:
    def __init__(self, rgb_path, thermal_path, depth_path):
        self.img1 = cv2.imread(rgb_path)
        self.img2 = cv2.imread(thermal_path)
        self.img3 = cv2.imread(depth_path)

        self.gray1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2GRAY)
        self.gray2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY)
        self.gray3 = cv2.cvtColor(self.img3, cv2.COLOR_BGR2GRAY)

        self.hist1 = cv2.calcHist([self.gray1], [0], None, [256], [0, 256])
        self.hist2 = cv2.calcHist([self.gray2], [0], None, [256], [0, 256])
        self.hist3 = cv2.calcHist([self.gray3], [0], None, [256], [0, 256])
        
    def plot_histograms(self):
        plt.figure(figsize=(10, 4))

        plt.subplot(131)
        plt.plot(self.hist1)
        plt.title("RGB")

        plt.subplot(132)
        plt.plot(self.hist2)
        plt.title("Thermal")

        plt.subplot(133)
        plt.plot(self.hist3)
        plt.title("Depth")

        plt.show()


# if __name__ == "__main__":
#     rgb_path = "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/RGB_15;01;10.jpg"
#     thermal_path = "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/Thermal_15;01;10.jpg"
#     depth_path = "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/Depth_15;01;10.jpg"
    
#     histograms = ImageHistograms3(rgb_path, thermal_path, depth_path)
#     histograms.plot_histograms()
