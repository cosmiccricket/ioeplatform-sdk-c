from sdk import Sdk
from location import Location
from user import User
from device import Device

'''
Created on June 27, 2013
@author: Arun Varma
'''

if __name__ == '__main__':
    loc = Location("id")
    '''print(loc.toJSON())'''
    User.login("asdf", "sadf")
    '''print(user1.toJSON())
    dev = Device(user1, "adf", loc)
    print(Sdk.toJson(dev))
    user1.createAccount("asdfsad", "asdfasd", "asdfds", loc, "Arun", "Varma")
    user1.login("asdfsad", "asdfasd")'''