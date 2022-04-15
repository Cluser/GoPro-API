from goprocam import GoProCamera, constants

def getRemainingSpace() -> int:
    goproCamera = GoProCamera.GoPro()
    remainingSpace = goproCamera.getStatus(constants.Status.Status, constants.Status.STATUS.RemainingSpace)
    print(remainingSpace)
    return remainingSpace
