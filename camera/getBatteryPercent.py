from goprocam import GoProCamera, constants

def getBatteryPercent() -> int:
    goproCamera = GoProCamera.GoPro()
    batteryPercent = goproCamera.getStatus(constants.Status.Status, constants.Status.STATUS.BattPercent)
    print(batteryPercent)
    return batteryPercent
