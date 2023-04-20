import MainRGB as cam
import cv2

cs = cam.CamStream(camera_index=1, width=640, height=480)


# Capture an image
while True:
    ret, frameC = cs.cam.read()

    if ret:
        cv2.imshow("Normal", frameC)
        # cv2.waitKey(5000)
        break


# cv2.imshow("Image", frameC)
# cv2.waitKey(1)

cs.cam.release()
cv2.destroyAllWindows()