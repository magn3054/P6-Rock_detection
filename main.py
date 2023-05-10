import cv2

path = "C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images"
if type(cv2.imread("C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;44;35.jpg")) == 'NoneType':
    print("The path exists!")

else:
    print("Changing path")
    path = "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/"


input_str = input("Enter task(s) to run (OTUS, hstogram, tempate, BLoB): ")
tasks = input_str.split()

RGBPath26 = f"{path}/26-04-2023/RGB_13;44;35.jpg"
ThermalPath26 = f"{path}/26-04-2023/Thermal_13;44;35.jpg"
DepthPath26 = f"{path}/26-04-2023/Depth_13;44;35.jpg"


RGB_paths26 = [
    f"{path}/26-04-2023/RGB_13;44;35.jpg",
    f"{path}/26-04-2023/RGB_13;45;44.jpg",
    f"{path}/26-04-2023/RGB_13;46;21.jpg",
    f"{path}/26-04-2023/RGB_13;47;11.jpg",
    f"{path}/26-04-2023/RGB_13;47;38.jpg",
    f"{path}/26-04-2023/RGB_13;48;05.jpg"
    ]

RGB_paths09 = [
    f"{path}/09-05-2023/RGB_12;50;13.jpg",
    f"{path}/09-05-2023/RGB_13;01;51.jpg",
    f"{path}/09-05-2023/RGB_13;07;41.jpg",
    f"{path}/09-05-2023/RGB_13;13;23.jpg",
    f"{path}/09-05-2023/RGB_13;16;23.jpg",
    f"{path}/09-05-2023/RGB_13;17;59.jpg",
    f"{path}/09-05-2023/RGB_13;18;13.jpg",
    f"{path}/09-05-2023/RGB_13;20;56.jpg",
    f"{path}/09-05-2023/RGB_13;21;12.jpg",
    f"{path}/09-05-2023/RGB_13;24;53.jpg",
    f"{path}/09-05-2023/RGB_13;26;04.jpg",
    f"{path}/09-05-2023/RGB_13;27;15.jpg",
    f"{path}/09-05-2023/RGB_13;28;46.jpg"
    ]

Thermal_paths26 = [
    f"{path}/26-04-2023/Thermal_13;44;35.jpg",
    f"{path}/26-04-2023/Thermal_13;45;44.jpg",
    f"{path}/26-04-2023/Thermal_13;46;21.jpg",
    f"{path}/26-04-2023/Thermal_13;47;11.jpg",
    f"{path}/26-04-2023/Thermal_13;47;38.jpg",
    f"{path}/26-04-2023/Thermal_13;48;05.jpg"
    ]

Thermal_paths09 = [
    f"{path}/09-05-2023/Thermal_12;50;13.jpg",
    f"{path}/09-05-2023/Thermal_13;01;51.jpg",
    f"{path}/09-05-2023/Thermal_13;07;41.jpg",
    f"{path}/09-05-2023/Thermal_13;13;23.jpg",
    f"{path}/09-05-2023/Thermal_13;16;23.jpg",
    f"{path}/09-05-2023/Thermal_13;17;59.jpg",
    f"{path}/09-05-2023/Thermal_13;18;13.jpg",
    f"{path}/09-05-2023/Thermal_13;20;56.jpg",
    f"{path}/09-05-2023/Thermal_13;21;12.jpg",
    f"{path}/09-05-2023/Thermal_13;24;53.jpg",
    f"{path}/09-05-2023/Thermal_13;26;04.jpg",
    f"{path}/09-05-2023/Thermal_13;27;15.jpg",
    f"{path}/09-05-2023/Thermal_13;28;46.jpg"
    ]

Depth_paths26 = [
    f"{path}/26-04-2023/Depth_13;44;35.jpg",
    f"{path}/26-04-2023/Depth_13;45;44.jpg",
    f"{path}/26-04-2023/Depth_13;46;21.jpg",
    f"{path}/26-04-2023/Depth_13;47;11.jpg",
    f"{path}/26-04-2023/Depth_13;47;38.jpg",
    f"{path}/26-04-2023/Depth_13;48;05.jpg"
    ]

Depth_paths09 = [
    f"{path}/09-05-2023/Thermal_12;50;13.jpg",
    f"{path}/09-05-2023/Thermal_13;01;51.jpg",
    f"{path}/09-05-2023/Thermal_13;07;41.jpg",
    f"{path}/09-05-2023/Thermal_13;13;23.jpg",
    f"{path}/09-05-2023/Thermal_13;16;23.jpg",
    f"{path}/09-05-2023/Thermal_13;17;59.jpg",
    f"{path}/09-05-2023/Thermal_13;18;13.jpg",
    f"{path}/09-05-2023/Thermal_13;20;56.jpg",
    f"{path}/09-05-2023/Thermal_13;21;12.jpg",
    f"{path}/09-05-2023/Thermal_13;24;53.jpg",
    f"{path}/09-05-2023/Thermal_13;26;04.jpg",
    f"{path}/09-05-2023/Thermal_13;27;15.jpg",
    f"{path}/09-05-2023/Thermal_13;28;46.jpg"
    ]

if "otsu" or "OTSU" in tasks:
    ### OTSU ###
    import OTSU
    print("Doing OTSU")
    for Thermal_imgs in Thermal_paths09:
        otsuSingle = OTSU.OtsuThresholding1(Thermal_imgs)
        otsuSingle.display_images()

    # otsuTrio = OTSU.OtsuThresholding3(RGBPath, ThermalPath, DepthPath)
    # otsuTrio.display_images()


if "hist" or "histogram" in tasks:
    ### Histogram ###
    import Histogram as hist
    print("Doing Histogram")

    histogram = hist.ImageHistograms1(f"{path}/templates/template_13;47;11.jpg")
    histogram.plot_histograms()

    Hnr = 0
    for RGB, thermal, depth in zip(RGB_paths09, Thermal_paths09, Depth_paths09): 
        
        cv2.imshow("RGB",cv2.imread(RGB))
        cv2.imshow("Thermal",cv2.imread(thermal))
        Hnr += 1
        print(f"Histogram nr. {Hnr}")
        histograms = hist.ImageHistograms3(RGB, thermal, depth)
        histograms.plot_histograms()
        cv2.destroyAllWindows


if "template" or "temp" in tasks:
    ### Template matching ###
    import TemplateMatcher as TM
    print("Doing Template matcher")
    for RGB_imgs in RGB_paths09:
        matcher = TM.TemplateMatcher(RGB_imgs)
        matcher.add_template(f"{path}/templates/template_13;47;11.jpg")
        matcher.add_template(f"{path}/templates/template_13;47;38.jpg")
        matcher.add_template(f"{path}/templates/template_13;48;05.jpg")
        matcher.match_templates()
        matcher.show_result()

## virker ikke ##
# import hist_compare as HC

# compare = HC.RockHistogram(RGBPath, [120,20,180], [160,60,255], 5)
# compare.classify_rock_regions('C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;11.jpg')

if "nope" or "nope1" in tasks:
    ### Histogram matcher ###
    import hist_matcher as HM
    print("Doing Histogram matcher")
    kernel_size = 6
    templates = [
        f'{path}/templates/template_13;47;11.jpg',
        f'{path}/templates/template_13;47;38.jpg',
        f'{path}/templates/template_13;48;05.jpg'
    ]

    HistMatch = HM.HistogramMatcher(templates,RGB_paths26,kernel_size)
    HistMatch.match_templates()

if "blob" or "BLOB" in tasks:
    ### BLOB ###
    import Thermal.BLOB as BLOB
    BB = BLOB.BLOB()
    BB.blobber(Thermal_paths09)


else:
    print("Task not recognized")