import cv2
import numpy as np
import hist_matcher as HM

class TemplateMatcher:
    def __init__(self, main_img_path):
        self.main_img = cv2.imread(main_img_path)
        self.templates = []
        self.existing_rectangles = []
        self.poss_rock = []

    def add_template(self, template_path):
        template = cv2.imread(template_path)
        self.templates.append(template)

    def match_templates(self):
        nr = 0
        self.mask = np.zeros_like(self.main_img[:, :, 0])
        for template in self.templates:
            res = cv2.matchTemplate(self.main_img, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            h, w = template.shape[:-1]
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # check if there is already a red rectangle at the location of the new rectangle - rectangles may overlap with 10%
            if not any((top_left[0] <= pt2[0] * 0.90 and pt1[0] <= bottom_right[0] * 0.90 and
                        top_left[1] <= pt2[1] * 0.90 and pt1[1] <= bottom_right[1] * 0.90) for pt1, pt2 in self.existing_rectangles):
                cv2.rectangle(self.main_img, top_left, bottom_right, (0, 0, 255), 2)
                self.mask[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = 255
                # remember the location of the newly drawn rectangle
                self.existing_rectangles.append((top_left, bottom_right))
                nr += 1
        else:
            if nr == 1:
                print("Found 1 possible rock")
            else:
                print(f"Found {nr} possible rocks")

    def show_result(self):
        masked_img = cv2.bitwise_and(self.main_img, self.main_img, mask=self.mask)
        transparency = 0.5
        overlay = np.zeros_like(self.main_img)
        overlay[self.mask > 0] = (255, 255, 255)
        overlay = cv2.addWeighted(self.main_img, 1-transparency, overlay, transparency, 0)
        result = cv2.addWeighted(masked_img, 1-transparency, overlay, transparency, 0)
        cv2.imshow('Masked', result)
        cv2.waitKey(0)

    # def compare(self, templates):
    #     x1, y1 = redbox[0]
    #     x2, y2 = redbox[1]
    #     #region = self.main_img[y1:y2, x1:x2, :]
    #     gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    #     for template in templates:
    #         matched = HM.match_histograms(gray, template)
    #         similarity = np.sum(np.abs(matched - template))
    #         if similarity < threshold:
    #             self.poss_rock.append(redbox)