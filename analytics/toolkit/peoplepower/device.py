from sdk import Sdk
import http.client as http, urllib

'''
Created on June 25, 2013
@author: Arun Varma
'''

class Device(object):
    '''
    __init__
    defines a device object with a unique deviceId and a location
    @param deviceId: String (case sensitive with no spaces)
    @param desc: String (user description of the device)
    @param loc: Location
    '''
    '''
    ACCEPTS EVERYTHING SUPPORTED IN URL
    '''
    def __init__(self, deviceId, user, desc, loc):
        for char in deviceId:
            if char == " ":
                raise Exception("Device ID can only take valid characters")
        self.id = deviceId
        self.user = user
        self.desc = desc
        self.location = loc
        '''
        self._conn = http.client("https://developer.peoplepowerco.com")
        '''

    '''
    refreshDevicesFromServer
    ?????????????????????????
    '''
    def refreshDevicesFromServer(self):
        return

    '''
    register
    registers this device with the cloud
    '''
    @staticmethod
    def register(productId, deviceId, loc):
        '''
        siteExt = "/cloud/xml/deviceRegistration/" + loc.??? + "/" + deviceId
        params = {}
        params["productId"] = Sdk.getProductId(productId)
        header = {"PRESENCE_API_KEY" : loc.getUser().getApiKey()}
        conn = http.HTTPSConnection(Sdk.rootSite(), 443)
        conn.connect()
        conn.request("POST", siteExt, urllib.parse.urlencode(params), header)
        print(conn.getresponse().read())
        '''
        return

    '''
    populate
    populates specified parameters of this device with current information
    if params is not specified, the last known parameters will be populated
    @param params: Parameter[]
    '''
    def populate(self, params = None):
        if params == None:
            params = self.getParams()

    '''
    getDeviceId
    returns the ID number of this device
    '''
    def getId(self):
        return self.id

    '''
    getLocation
    returns the location of this device
    '''
    def getLocation(self):
        return self.loc

    '''
    getParams
    gets specified parameters of this device
    if params is not specified, will return the last known parameters
    @param params: Parameter
    '''
    def getParams(self, params = None):
        return