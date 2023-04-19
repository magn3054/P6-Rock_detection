import cv2

class CamStream:
    def __init__(self, camera_index=0, width=640, height=480):
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.cam = cv2.VideoCapture(camera_index)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    
    def run(self):
        while True:
            ret, Cframe = self.cam.read()
    
            if ret:
                Cframe = cv2.resize(Cframe, (self.width, self.height))
                cv2.imshow("Normal", Cframe)
        
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                break
    
        self.cam.release()
        cv2.destroyAllWindows()
