'''
Created on Aug 7, 2013
@author: Arun Varma
'''
import datetime, pytz, time, dateutil.parser as dateutil


ON = "ON"
OFF = "OFF"
OUTLET_STATUS = "outletStatus"
LAST_UPDATE_TIME = "lastUpdateTime"
DEFAULT_TIME = 5
DEFAULT_PRODUCT_ID = 2012
DAYS_MINUTES_FACTOR = 1440


'''
run
@param user: User
turns the user's default devices off automatically after the default time
'''
def run(user):
    # timerOff all devices with the default product id
    devices = user.getDevicesByProductId(DEFAULT_PRODUCT_ID)
    for device in devices:
        timerOff(device, DEFAULT_TIME)


'''
timerOff
@param device: Device
@param minutes: int
turns the given device off automatically after the given time
'''
def timerOff(device, minutes):
    # only timerOff if device is already on
    if isOn(device):
        # get the time the device was turned on last
        lastUpdate = isoToDate(device.getParameter(OUTLET_STATUS)[LAST_UPDATE_TIME])
        # find the time the device should turn off; device to get minutes from days
        delta = datetime.timedelta(minutes / DAYS_MINUTES_FACTOR)
        turnOffTime = lastUpdate + delta

        # subtract to find amount of time from now till device turnoff
        tz = pytz.timezone("MST")
        now = tz.localize(datetime.datetime.now())
        timeTillOff = (turnOffTime - now).total_seconds()
        print(timeTillOff)

        # if device should not turn off yet, wait until then; turn off device
        if timeTillOff >= 0:
            time.sleep(timeTillOff)
        turnOffOutletStatus(device)


'''
turnOffOutletStatus
@param device: Device
turn device's outletStatus off
'''
def turnOffOutletStatus(device):
    device.sendCommand(OUTLET_STATUS, None, OFF)


'''
switchOutletStatus
@param device: Device
if the device's outletStatus is off, turn it on; else, turn it off
@return device's outletStatus
'''
def switchOutletStatus(device):
    if isOn(device):
        device.sendCommand(OUTLET_STATUS, None, OFF)
    else:
        device.sendCommand(OUTLET_STATUS, None, ON)
    return device.populateParams([OUTLET_STATUS])


'''
isOn
@param device: Device
@return true if the device's outletStatus is on; false otherwise
'''
def isOn(device):
    return device.getParameter(OUTLET_STATUS)["value"] == ON

'''
isoToDate
@param iso: String
converts an ISO DateTime to a Python DateTime
'''
def isoToDate(iso):
    return dateutil.parse(iso)