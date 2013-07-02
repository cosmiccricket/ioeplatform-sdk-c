from sdk import Sdk
import http.client as http, urllib.parse

'''
Created on June 25, 2013
@author: Arun Varma
'''

class User(object):
    '''
    __init__
    defines a User object with a unique userId and list of locations where they have put devices
    @param apiKey: String
    '''
    def __init__(self, username, password):
        self.apiKey = self.login(username, password)
        '''
        self.username = username
        self.password = password
        self.appname = appName
        self.location = loc
        self.firstname = firstName
        self.lastname = lastName
        '''

    '''
    createAccount
    creates an account for a new User
    @param: username: String (email address)
    @param password: String
    @param appName: String
    @param loc: Location
    @param firstName: String (optional)
    @param lastName: String (optional)
    '''
    def createAccount(self, username, password, appName, loc, firstName = None, lastName = None):
        siteExt = "/cloud/json/newUser"
        body = self.toJSON()
        header = {"Content-Type" : "application/json"}
        conn = http.HTTPSConnection(Sdk.rootSite(), 443)
        conn.connect()
        conn.request("POST", siteExt, body, header)
        result = conn.getresponse()
        '''
        result = json.loads(conn.getresponse().read())
        '''
        print(result.read())

    '''
    login
    @return the User's API Key
    @param username: String (email address)
    @param password: String
    '''
    @staticmethod
    def login(username, password):
        siteExt = "/cloud/login"
        params = {}
        params["username"] = username
        header = {"PASSWORD" : password}
        conn = http.HTTPSConnection(Sdk.rootSite(), 443)
        conn.connect()
        conn.request("POST", siteExt, urllib.parse.urlencode(params), header)
        apiKey = conn.getresponse().read()
        print(apiKey)
        return apiKey

    '''
    refreshFromServer
    refreshes User's information
    '''
    def refreshFromServer(self):
        siteExt = "/cloud/json/user"
        params = {}
        params["username"] = self.username
        header = {"PRESENCE_API_KEY" : self.apiKey}
        conn = http.HTTPSConnection(Sdk.rootSite(), 443)
        conn.connect()
        conn.request("GET", siteExt, urllib.parse.urlencode(params), header)
        print(conn.getresponse().read())

    '''
    addLocation
    adds a location to this User's list of locations
    @param loc: Location
    '''
    def addLocation(self, loc):
        self.locations.add(loc)

    '''
    getLocations
    @return this User's list of locations
    '''
    def getLocations(self):
        return self.locations

    '''
    getId
    @return the ID number of this User
    '''
    def getId(self):
        return self.id

    '''
    getApiKey
    @return the API Key of this User
    '''
    def getApiKey(self):
        return