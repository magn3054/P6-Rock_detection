import cv2
import numpy as np
import matplotlib.pyplot as plt

def align_images(thermal_image_path, rgb_image_path):
    # Load thermal image
    img = cv2.imread(thermal_image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Mask for orange and yellow
    radius = 7
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*radius+1, 2*radius+1))
    lower = np.array([14, 182, 241])
    upper = np.array([34, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel2)

    # Apply mask to original image
    merged = cv2.bitwise_and(img, img, mask=mask)
    merged2 = merged.copy()

    # BLOB
    pixels = merged2.reshape((-1, 3))
    pixels = np.float32(pixels)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 3
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    res2 = res.reshape((merged2.shape))

    # Use connected component analysis to separate the individual blobs
    components, labels, stats, centroids= cv2.connectedComponentsWithStats(mask) 
    # stats return the xpos[0], ypos[1], width[2], height[3] and area[4] of the different blobs
    rois=[]
    for i in range(1, len(stats)): 
        x = stats[i][0]
        y = stats[i][1]
        w = stats[i][2]
        h = stats[i][3]
        roi = (x, y, w, h)
        rois.append(roi)

    new_value = 0  # black pixel

    for i, (x, y, w, h) in enumerate(rois):
        # Extract region of interest
        roi = res2[y:y+h, x:x+w]
        
        # Compute color histogram
        hist = cv2.calcHist([res2], [0, 1], None, [180, 256], [0, 180, 0, 256])
        
        # find colors present in region 
        color_threshold = 50 # filters out color with low saturation/brightness such as black 
        colors = []
        for row in roi: 
            for pixel in row:
                hue,sat,val = pixel
                if sat > color_threshold and val > color_threshold:
                    hue_bin = int(hue)
                    colors.append(hue_bin) 
        
        color_counts = np.bincount(colors)
        color_counts = np.concatenate([color_counts, np.zeros(180-len(color_counts), dtype=int)])
        

        if color_counts[3] > color_counts[18]:
            for row in range(roi.shape[0]):
                for col in range(roi.shape[1]):
                    roi[row, col] = new_value        

    # Resize thermal image to match RGB image size
    rgb_image = cv2.imread(rgb_image_path)
    resized_thermal_image = cv2.resize(res2, (rgb_image.shape[1], rgb_image.shape[0]))

    # Find contours
    gray = cv2.cvtColor(resized_thermal_image, cv2.COLOR_BGR2GRAY)
    ret, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contour rings on RGB image
    output_image = rgb_image.copy()
    for cnt in contours:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        arclength = cv2.arcLength(cnt, True) ** 2
        if arclength == 0:
            arclength += 0.01
        circularity = 4 * 3.15 * cv2.contourArea(cnt) / arclength
        if circularity >= 0.5 and radius >= 7:
            cv2.putText(output_image, "rock", (int(x - radius), int(y - radius - 10)),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0), 2)
            cv2.circle(output_image, center, radius, (0, 255, 0), 2)

    # Display output image
    cv2.imshow('Output Image', output_image)
    cv2.imshow('resized_thermal_image', resized_thermal_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the file paths of the thermal and RGB images
thermal_image_path = "./Images/10-05-2023/Thermal_09;32;22.jpg"
rgb_image_path = "./Images/10-05-2023/RGB_09;32;22.jpg"

# Call the align_images function
align_images(thermal_image_path, rgb_image_path)
