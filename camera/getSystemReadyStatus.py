from goprocam import GoProCamera, constants

def getSystemReadyStatus() -> bool:
    goproCamera = GoProCamera.GoPro()
    systemReadyStatus = goproCamera.getStatus(constants.Status.Status, constants.Status.STATUS.SystemReady)
    print(systemReadyStatus)
    return systemReadyStatus
