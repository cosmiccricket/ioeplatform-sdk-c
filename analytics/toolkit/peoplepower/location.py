'''
Created on June 25, 2013
@author: Arun Varma
'''

class Location(object):
    '''
    __init__
    defines a Location object
    @param name: String
    @param state: State
    @param country: Country
    @param city: String
    @param timezone: Timezone
    @param zipcode: String
    '''
    def __init__(self, name, timezone = None, address1 = None, address2 = None, city = None, state = None, country = None, zipcode = None):
        self.name = name
        self.timezone = timezone
        self.addrstreet1 = address1
        self.addrstreet2 = address2
        self.addrcity = city
        self.state = state
        self.country = country
        self.zip = zipcode

    '''
    refreshFromServer
    ????????????????????????????//
    '''
    def refreshFromServer(self):
        return

    '''
    addDevice
    adds the given device to this Location's list of devices
    @param device: Device
    '''
    def addDevice(self, device):
        self.devices.add(device)

    '''
    getDevices
    @return the list of Devices at this Location
    '''
    def getDevices(self):
        return self.devices

    '''
    getUser
    @return the user at this Location
    '''
    def getUser(self):
        return

    '''
    getName
    @return the name of this Location
    '''
    def getName(self):
        return self.name

    '''
    getTimezone
    @return the timezone of this Location
    '''
    def getTimezone(self):
        return self._timezone

    '''
    getAddress1
    @return the first address of this Location
    '''
    def getAddress1(self):
        return self.addrstreet1

    '''
    getAddress2
    @return the second address of this Location
    '''
    def getAddress2(self):
        return self.addrstreet2

    '''
    getCity
    @return the city of this Location
    '''
    def getCity(self):
        return self.addrcity

    '''
    getState
    @return the state of this Location
    '''
    def getState(self):
        return self.state

    '''
    getCountry
    @return the country of this Location
    '''
    def getCountry(self):
        return self.country

    '''
    getZipcode
    @return the zipcode of this Location
    '''
    def getZipcode(self):
        return self.zip