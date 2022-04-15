from goprocam import GoProCamera, constants
import time


def cmdStartRecording() :
    goproCamera = GoProCamera.GoPro()
    goproCamera.mode(constants.Mode.VideoMode)
    goproCamera.video_settings('1080p', '200')
    time.sleep(1)
    goproCamera.shutter(constants.start)








