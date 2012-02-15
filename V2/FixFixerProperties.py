class DefaultTags():
    def __init__(self):
        self.__properties = dict()

    def GetProperties(self):
        retList = []
        for key in self.__properties.keys():
            string = str(key) + "=" + str(self.__properties[key])
            retList.append(string)
        return retList
    
    def SetProperty(self, key, value):
        self.__properties[key] = value
        
    def GetProperty(self,key):
        if key in self.__properties:
            return self.__properties[key]
        else:
            return Null
        
class FixFixerProperties:
    def __init__(self):
        self.__properties = dict()

    def SetProperty(self, property, value):
        self.__properties[property] = value

    def GetProperty(self, property):
        return self.__properties[property]

    
