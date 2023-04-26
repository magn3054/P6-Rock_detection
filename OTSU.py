import cv2

class OtsuThresholding1:
    
    def __init__(self, img_path):
        self.img_path = img_path
        self.img_gray = None
        self.img_binary = None
    
    def load_image(self):
        self.img_gray = cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)
    
    def apply_otsu_thresholding(self):
        if self.img_gray is None:
            self.load_image()
        _, self.img_binary = cv2.threshold(self.img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    def display_images(self):
        if self.img_gray is None or self.img_binary is None:
            self.apply_otsu_thresholding()
        cv2.imshow('Original Image', self.img_gray)
        cv2.imshow('Binary Image', self.img_binary)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




class OtsuThresholding3:
    
    def __init__(self, RGB_path, Thermal_path, Depth_path):
        self.RGB_path = RGB_path
        self.Thermal_path = Thermal_path 
        self.Depth_path = Depth_path
        self.RGB_gray = None
        self.Thermal_gray = None
        self.Depth_gray = None
        self.RGB_binary = None
        self.Thermal_binary = None
        self.Depth_binary = None
    
    def load_image(self):
        self.RGB_gray = cv2.imread(self.RGB_path, cv2.IMREAD_GRAYSCALE)
        self.Thermal_gray = cv2.imread(self.Thermal_path, cv2.IMREAD_GRAYSCALE)
        self.Depth_gray = cv2.imread(self.Depth_path, cv2.IMREAD_GRAYSCALE)
    
    def apply_otsu_thresholding(self):
        if self.RGB_gray is None or self.Thermal_gray is None or self.Depth_gray is None:
            self.load_image()
        _, self.RGB_binary = cv2.threshold(self.RGB_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        __, self.Thermal_binary = cv2.threshold(self.Thermal_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ___, self.Depth_binary = cv2.threshold(self.Depth_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    def display_images(self):
        if self.RGB_gray is None or self.Thermal_gray is None or self.Depth_gray is None or self.RGB_binary is None or self.Thermal_binary is None or self.Depth_binary is None:
            self.apply_otsu_thresholding()
        cv2.imshow('Original Image', self.RGB_gray)
        cv2.imshow('Binary RGB Image', self.RGB_binary)
        cv2.imshow('Binary Thermal Image', self.Thermal_binary)
        cv2.imshow('Binary Depth Image', self.Depth_binary)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()



if __name__ == "__main__":
    otsu = OtsuThresholding1('image.png')
    otsu.display_images()


# if __name__ == "__main__":
#     otsu = OtsuThresholding('C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/RGB_15;01;10.jpg')
#     otsu.display_images()