from fastapi import APIRouter
import camera

router = APIRouter()

@router.get("/CmdInitConnection", tags=["GoPro"])
async def get():
    await camera.cmdInitConnection()

@router.get("/CmdPowerOff", tags=["GoPro"])
async def get():
    return camera.cmdPowerOff()

@router.get("/CmdPowerOn", tags=["GoPro"])
async def get():
    return camera.cmdPowerOn()

@router.get("/StartRecording", tags=["GoPro"])
async def get():
    return camera.cmdStartRecording()

@router.get("/StopRecording", tags=["GoPro"])
async def get(path: str = 'DefaultFolder', filename: str = 'DefaultFileName'):
    return camera.cmdStopRecording(path, filename)

@router.get("/GetBatteryPercent", tags=["GoPro"])
async def get():
    return camera.getBatteryPercent()

@router.get("/GetBusyStatus", tags=["GoPro"])
async def get():
    return camera.getBusyStatus()

@router.get("/GetRecordingStatus", tags=["GoPro"])
async def get():
    return camera.getRecordingStatus()

@router.get("/GetRemainingSpace", tags=["GoPro"])
async def get():
    return camera.getRemainingSpace()

@router.get("/GetSystemReadyStatus", tags=["GoPro"])
async def get():
    return camera.getSystemReadyStatus()







        


