from goprocam import GoProCamera, constants

def getRecordingStatus() -> bool:
    goproCamera = GoProCamera.GoPro()
    recordingStatus = goproCamera.getStatus(constants.Status.Status, constants.Status.STATUS.IsRecording)
    print(recordingStatus)
    return recordingStatus

