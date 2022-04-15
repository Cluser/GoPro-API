import asyncio
from camera.commands import *
import pywifi
from typing import List
from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice

from pywifi import const

# Config
# CFG_CAMERA_WIFI_SSID = 'GP50851023'
# CFG_CAMERA_WIFI_PASSWORD  = 'hKC-w9s-QN9'
CFG_CAMERA_WIFI_SSID = 'GP28904668'
CFG_CAMERA_WIFI_PASSWORD  = 'Sc8-swc-QHq'


async def cmdInitConnection() -> None:
    devices = await discoverDevices()
    goproDeviceAddress = await getGoProAddress(devices)
    connectedDevice = await connectToDevice(goproDeviceAddress)

    async with connectedDevice:
        await turnOnWifi(connectedDevice)


async def discoverDevices() -> None: 
    return await BleakScanner.discover()


async def getGoProAddress(devices: List[BLEDevice]) -> str:
    for device in devices:
        print(device)
        if "GoPro" in str(device.name):
            print(device.address)
            return device.address
            

async def connectToDevice(address: str) -> BleakClient:
    return BleakClient(address)


async def turnOnWifi(client: BleakClient) -> None:
    await client.write_gatt_char(Characteristics.ControlCharacteristic, Commands.WiFi.ON)
    await connectToWifi()


async def connectToWifi() -> None:
    print('Connecting to WiFi')

    wifi = pywifi.PyWiFi()

    interface = wifi.interfaces()[0]

    profile = pywifi.Profile()
    profile.ssid = CFG_CAMERA_WIFI_SSID
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = CFG_CAMERA_WIFI_PASSWORD

    savedProfile = interface.add_network_profile(profile)

    interface.connect(savedProfile)

    print('Connected to WiFi')


