from goprocam import GoProCamera

def cmdPowerOff() -> None:
    goproCamera = GoProCamera.GoPro()
    goproCamera.power_off()
