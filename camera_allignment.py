import cv2
import numpy as np

def align_images(thermal_image_path, rgb_image_path):
    # Load thermal image
    thermal_image = cv2.imread(thermal_image_path, 0)  # Read as grayscale
    rgb_image = cv2.imread(rgb_image_path)

    # Resize the thermal image to match the size of the RGB image
    resized_thermal_image = cv2.resize(thermal_image, (rgb_image.shape[1], rgb_image.shape[0]))

    # Define the transformation matrix
    rotation_matrix = cv2.getRotationMatrix2D((rgb_image.shape[1] // 2, rgb_image.shape[0] // 2), 0, 1)
    translation_matrix = np.float32([[1, 0, 0], [0, 1, -5], [0, 0, 1]])  # 5 cm translation along z-axis (behind thermal lens)
    transformation_matrix = np.matmul(rotation_matrix, translation_matrix)

    # Apply the transformation to the RGB image
    aligned_rgb_image = cv2.warpAffine(rgb_image, transformation_matrix, (rgb_image.shape[1], rgb_image.shape[0]))

    # Display the aligned images
    cv2.imshow("Aligned Thermal Image", resized_thermal_image)
    cv2.imshow("Aligned RGB Image", aligned_rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the file paths of the thermal and RGB images
thermal_image_path = "./Images/10-05-2023/Thermal_09;41;08.jpg"
rgb_image_path = "./Images/10-05-2023/RGB_09;41;08.jpg"

# Call the align_images function
align_images(thermal_image_path, rgb_image_path)