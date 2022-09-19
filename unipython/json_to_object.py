'''
This module contains class for json-to-object serialization
'''


class JsonObject:
    ''' This class serializes a dictionary to JsonObject'''

    def __init__(self, data:dict):
        for key in data:
            attr = key
            if attr == "from": attr = "from_" 
            if not isinstance(data[key], dict):
                self.__setattr__(attr, data[key])
            else:
                self.__setattr__(attr, JsonObject(data[key]))
    
    def get_attr(self):
        return self.__dict__

    def __str__(self):
        return f"<{self.__class__.__name__}>"

    def __repr__(self):
        return f"<{self.__class__.__name__}>"
