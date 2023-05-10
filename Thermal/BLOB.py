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

class BLOB:
    def blobber(self, therm_path):

        it = 0

        for imgs in therm_path:
            it += 1
            # Load imageThermal_13;23;45.jpg
            img = cv2.imread(imgs)
            # img = img[225:600, 0:800]
            # Reshape image into a 2D array of pixels
            pixels = img.reshape((-1, 3))

            # Convert pixel values to float32 for k-means clustering
            pixels = np.float32(pixels)

            # Define k-means parameters
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            k = 5  # number of clusters

            # Run k-means clustering
            _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

            # Convert centers back to uint8 and reshape to match image shape
            centers = np.uint8(centers)
            res = centers[labels.flatten()]
            res2 = res.reshape((img.shape))

            # Display segmented image
            cv2.imshow(f'segmented image {it}', res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
