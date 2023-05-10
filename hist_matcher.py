import cv2
import numpy as np

class HistogramMatcher:
    def __init__(self, templates, input_images, kernel_size):
        self.templates = templates
        self.input_images = input_images
        if kernel_size % 2 == 0:
            kernel_size+=1  
        self.kernel_size = kernel_size
        self.hist_templates = []
        self.masks = []
        self.results = []


    def calculate_histograms(self):
        for template in self.templates:
            # Calculate the histogram of each template image
            template = cv2.imread(template)
            hist = cv2.calcHist([cv2.cvtColor(template, cv2.COLOR_BGR2HSV)], [0, 1], None, [180, 256], [0, 180, 0, 256])
            # Normalize the histogram
            cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
            self.hist_templates.append(hist)

    def create_masks(self, img):
        for hist in self.hist_templates:
            # Create a mask for each template based on the color space
            mask = cv2.calcBackProject([cv2.cvtColor(img, cv2.COLOR_BGR2HSV)], [0, 1], hist, [0, 180, 0, 256], 1)
            mask = cv2.medianBlur(mask, self.kernel_size)
            self.masks.append(mask)

    def apply_masks(self, img):
        for mask in self.masks:
            # Apply each mask to the input image
            result = cv2.bitwise_and(img, img, mask=mask)
            self.results.append(result)

    def match_templates(self):
        self.calculate_histograms()
        for img_path in self.input_images:
            # Load the input image
            img = cv2.imread(img_path)

            self.create_masks(img)
            self.apply_masks(img)

            # Display the results
            for i, result in enumerate(self.results):
                cv2.imshow(f'Template {i+1} Result', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# if __name__ == "__main__":
#     templates = [
#         f'{path}templates/template_13;47;11.jpg',
#         f'{path}templates/template_13;47;38.jpg',
#         f'{path}templates/template_13;48;05.jpg'
#     ]

#     input_images = [
#         f'{path}26-04-2023/RGB_13;44;35.jpg',
#         f'{path}26-04-2023/RGB_13;45;44.jpg',
#         f'{path}26-04-2023/RGB_13;46;21.jpg'
#     ]

#     KernelSize = 10

#     TM = HistogramMatcher(templates, input_images, KernelSize)
#     TM.match_templates()