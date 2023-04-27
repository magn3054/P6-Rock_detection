RGBPath = 'C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;44;35.jpg'
ThermalPath = 'C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;44;35.jpg'
DepthPath = 'C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;44;35.jpg'


RGB_paths = [
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;44;35.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;45;44.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;46;21.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;11.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;38.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;48;05.jpg"
    ]

Thermal_paths = [
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;44;35.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;45;44.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;46;21.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;47;11.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;47;38.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Thermal_13;48;05.jpg"
    ]

Depth_paths = [
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;44;35.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;45;44.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;46;21.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;47;11.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;47;38.jpg",
    "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/Depth_13;48;05.jpg"
    ]

### OTSU ###
import OTSU

for Thermal_img in Thermal_paths:
    otsuSingle = OTSU.OtsuThresholding1(Thermal_img)
    otsuSingle.display_images()

# otsuTrio = OTSU.OtsuThresholding3(RGBPath, ThermalPath, DepthPath)
# otsuTrio.display_images()


### Histogram ###
import Histogram as hist

histograms = hist.ImageHistograms1("C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;47;11.jpg")
histograms.plot_histograms()

histograms = hist.ImageHistograms3(RGBPath, ThermalPath, DepthPath)
histograms.plot_histograms()


### Template matching ###
import TemplateMatcher as TM

for RGB_img in RGB_paths:
    matcher = TM.TemplateMatcher(RGB_img)
    matcher.add_template('C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;47;11.jpg')
    matcher.add_template('C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;47;38.jpg')
    matcher.add_template('C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;48;05.jpg')
    matcher.match_templates()
    matcher.show_result()


# import 