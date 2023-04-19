import cv2

# rtsp://<username>:<password>@<ip-address>/axis-media/media.amp
rtsp_url = "rtsp://root:kamera@169.254.104.184/axis-media/media.amp"

class ThermalStream:
    def __init__(self, camera_index=rtsp_url, width=640, height=480):
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.cam = cv2.VideoCapture(camera_index)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def run(self):
        while True:
            ret, Tframe = self.cam.read()
    
            if ret:
                Cframe = cv2.resize(Tframe, (self.width, self.height))
                cv2.imshow("Normal", Tframe)
        
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                break
    
        self.cam.release()
        cv2.destroyAllWindows()