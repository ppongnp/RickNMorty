import requests
import json
from character import Character

class HandleRequest():
    def __init__(self):
        self.URL = "https://rickandmortyapi.com/api/character/"
        self.character = []
    
    def getAll(self,URL):
        return requests.get(self.URL).json()

    def getByPage(self,number):
        return requests.get(self.URL + "?page=" + str(number)).json()
    
    def getById(self,ID):
        return requests.get(self.URL + str(ID)).json()
    
    def addCharacter(self):
        for i in range(1,26):
            response = self.getByPage(i)
            for item in response["results"]:
                temp = Character(item["id"],item["name"],item["status"],item["species"],\
                    item["type"],item["origin"],item["location"],item["image"],item["episode"],\
                    item["url"],item["created"] )
                self.character.append(temp)
    
    def listByCreated(self):
        result = []
        for item in self.character:
            if item.getCreated() == "2018-05-22" and item.getChar_name not in result:
                result.append(item.getChar_name())

        return result
if __name__ == "__main__":
    test = HandleRequest()
    test.addCharacter()
    print(test.listByCreated())

