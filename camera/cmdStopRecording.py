from os import mkdir
from goprocam import GoProCamera, constants
import time


def cmdStopRecording(path: str = 'DefaultFolder', filename: str = 'DefaultFileName') -> None:
    goproCamera = GoProCamera.GoPro()
    goproCamera.shutter(constants.stop)
    time.sleep(1)
    mkdir(path)
    goproCamera.downloadLastMedia('', path + '/' + filename + '.avi')




