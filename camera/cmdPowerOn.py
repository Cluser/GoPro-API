from goprocam import GoProCamera

def cmdPowerOn(address: str) -> None:
    goproCamera = GoProCamera.GoPro()
    goproCamera.power_on(address)