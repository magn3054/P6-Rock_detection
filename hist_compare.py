import cv2
import numpy as np

class RockHistogram:
    def __init__(self, img_path, lower_rock, upper_rock, median_kernel_size=5):
        self.img_path = img_path
        self.lower_rock = np.array(lower_rock)
        self.upper_rock = np.array(upper_rock)
        self.median_kernel_size = median_kernel_size
        self.rock_histograms = []

    def load_image(self):
        self.img = cv2.imread(self.img_path)
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def threshold_image(self):
        self.mask = cv2.inRange(self.hsv, self.lower_rock, self.upper_rock)
        self.mask = cv2.medianBlur(self.mask, self.median_kernel_size)
        # cv2.imshow("mask", self.mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

# # Define range of rock colors in HSV
# lower_rock = np.array([120,20,180])
# upper_rock = np.array([160,60,255])


    def find_contours(self):
        contours, _ = cv2.findContours(self.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.contours = contours

# Calculate histogram for each rock region
    def calculate_histograms(self):
        for contour in self.contours:
            # Extract rock region from mask
            x, y, w, h = cv2.boundingRect(contour)
            rock_mask = np.zeros(self.mask.shape, np.uint8)
            cv2.drawContours(rock_mask, [contour], 0, 255, -1)
            rock_mask = rock_mask[y:y+h, x:x+w]
            # Convert rock region to HSV color space
            rock_hsv = cv2.cvtColor(self.img[y:y+h, x:x+w], cv2.COLOR_BGR2HSV)
            # Calculate histogram for rock region
            rock_hist = cv2.calcHist([rock_hsv], [0, 1], rock_mask, [180, 256], [0, 180, 0, 256])
            # Normalize histogram
            cv2.normalize(rock_hist, rock_hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
            # Add histogram to list
            self.rock_histograms.append(rock_hist)


    def classify_rock_regions(self, new_image_path):
        # Load new image
        new_img = cv2.imread(new_image_path)
        # Convert new image to HSV color space
        new_hsv = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
        # Threshold new image to get potential rock regions
        new_mask = cv2.inRange(new_hsv, self.lower_rock, self.upper_rock)
        # Apply a median filter to remove noise
        new_mask = cv2.medianBlur(new_mask, self.median_kernel_size)
        # Find contours of potential rock regions
        new_contours, _ = cv2.findContours(new_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Create a list to store rock classifications
        rock_classifications = []

        # Calculate histogram for each potential rock region and compare with stored histograms
        for contour in new_contours:
            # Extract potential rock region from mask
            x, y, w, h = cv2.boundingRect(contour)
            potential_rock_mask = np.zeros(new_mask.shape, np.uint8)
            cv2.drawContours(potential_rock_mask, [contour], -1, (0, 255, 0), 2)
            potential_rock_mask = potential_rock_mask[y:y+h, x:x+w]
            # Convert potential rock region to HSV color space
            potential_rock_hsv = cv2.cvtColor(new_img[y:y+h, x:x+w], cv2.COLOR_BGR2HSV)
            # Calculate histogram for potential rock region
            potential_rock_hist = cv2.calcHist([potential_rock_hsv], [0, 1], potential_rock_mask, [180, 256], [0, 180, 0, 256])
            # Normalize histogram
            cv2.normalize(potential_rock_hist, potential_rock_hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
            # Calculate similarity between potential rock histogram and stored histograms
            similarities = []
            for rock_hist in self.rock_histograms:
                similarity = cv2.compareHist(rock_hist, potential_rock_hist, cv2.HISTCMP_CORREL)
                similarities.append(similarity)
            # Classify potential rock based on highest similarity
            if similarities:
                max_similarity = max(similarities)
                if max_similarity > 0.8:
                    rock_classifications.append(1) # Rock found
                else:
                    rock_classifications.append(0) # No rock found
            else:
                rock_classifications.append(0) # No rock found

        #Draw bounding boxes around classified rock regions
        for i, contour in enumerate(new_contours):
            if rock_classifications[i] == 1:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(new_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        #Display result
        cv2.imshow('Result', new_img)
        cv2.imshow('new mask', new_mask)
        cv2.imshow("mask", self.mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    RH = RockHistogram('C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;48;05.jpg', 
                       [120,20,180], [160,60,255], 5 )
    RH.load_image()
    RH.threshold_image()
    RH.classify_rock_regions('C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;11.jpg')

