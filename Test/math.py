# import math
import numpy as np
# set the object height in cm
object_height = 63

# set the POV angle in degrees
POV = np.deg2rad(40)

# set the image width and height in pixels
image_width = 1014
image_height = 570

# # # convert POV angle to radians
# # FOV = 2 * math.atan(math.tan(POV / 2) * (image_width / image_height))

# # calculate the distance in cm
distance = (object_height/2)/np.tan(POV/2)

# # print the result
# print("The object is approximately %.1f cm away from the camera." % distance)



