from goprocam import GoProCamera, constants

def getBusyStatus() -> bool:
    goproCamera = GoProCamera.GoPro()
    busyStatus = goproCamera.getStatus(constants.Status.Status, constants.Status.STATUS.IsBusy)
    print(busyStatus)
    return busyStatus
