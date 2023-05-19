import cv2
import requests

rtsp_url = "rtsp://root:kamera@169.254.104.185/axis-media/media.amp"
camera_ip = "169.254.104.185"

# Disable Automatic Gain Control (AGC)
agc_disable_url = f"http://{camera_ip}/axis-cgi/admin/param.cgi?action=update&root.ImageSource.I0.Sensor.AGC=off"
requests.get(agc_disable_url)

# Set a fixed color palette (White-hot)
color_palette_url = f"http://{camera_ip}/axis-cgi/admin/param.cgi?action=update&root.ImageSource.I0.Sensor.Palette=White-hot"
requests.get(color_palette_url)

# Create the ThermalStream class and run it
class ThermalStream:
    def __init__(self, camera_index=agc_disable_url, width=640, height=480):
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

if __name__ == "__main__":
    thermal_stream = ThermalStream()
    thermal_stream.run()
