import cv2
import numpy as np

paths26 = [
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;44;35.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;45;44.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;46;21.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;47;11.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;47;38.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;48;05.jpg"
]

blobs = [
            "imgblob2.jpg",
            "imgblob1.jpg",
            "imgblob3.jpg",
            "imgblob4.jpg",
            "imgblob5.jpg",
            "imgblob6.jpg",
            "imgblob7.jpg",
            "imgblob8.jpg",
            "imgblob9.jpg",
            "imgblob10.jpg",
            "imgblob11.jpg",
            "imgblob12.jpg",
            "imgblob13.jpg"            
        ]

class BLOB:
    def blobber(self, therm_path):
        it = 0
        imgnr = 0
        for imgs in therm_path:
            it += 1
            # Load image
            img = cv2.imread(imgs)
            # img = img[225:600, 0:800]
            # Reshape image into a 2D array of pixels
            print(f"image: \n{img.shape}")
            pixels = img.reshape((-1, 3))
            print(f"reshaped: \n{pixels.shape}")

            # Convert pixel values to float32 for k-means clustering
            pixels = np.float32(pixels)

            # Define k-means parameters
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            
            # Cluster size
            k = 2

            # Run k-means clustering
            _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
            
            # Convert centers back to uint8 and reshape to match image shape
            centers = np.uint8(centers)
            res = centers[labels.flatten()]
            res2 = res.reshape((img.shape))
            # self.blobbed = res2.tolist()
            imgnr += 1
            cv2.imwrite(f"img{imgnr}.jpg", res2)
            # Display segmented image
            cv2.imshow(f'segmented image {it}', res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()            


    def canny(self):
        print("Doing Canny")
        nr = 0

        for imgs in blobs:
            nr += 1
            # Load the image
            img = cv2.imread(imgs)
            # img = cv.resize(img, (400,800))

            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to reduce noise
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply Canny edge detection
            edges = cv2.Canny(gray, 1, 255)

            # Find contours in the edges image
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw contours on the original image
            cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

            # Display the result
            cv2.imshow(f'Edge {nr}', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()