import requests
import json
from character import Character
from PIL import Image
from io import BytesIO

class HandleRequest():
    def __init__(self):
        self.base_URL = "https://rickandmortyapi.com/api/character/"
        self.character = []
    
    def getAll(self,URL):
        return requests.get(self.base_URL).json()

    def getByPage(self,number):
        return requests.get(self.base_URL + "?page=" + str(number)).json()
    
    def getById(self,ID):
        return requests.get(self.base_URL + str(ID)).json()

    def testImage(self):
        response = requests.get("https://rickandmortyapi.com/api/character/avatar/1.jpeg")
        img = Image.open(BytesIO(response.content))
    
    def addCharacter(self):
        for i in range(1,26):
            response = self.getByPage(i)
            for item in response["results"]:
                temp = Character(item["id"],item["name"],item["status"],item["species"],\
                    item["type"],item["origin"],item["location"],item["image"],item["episode"],\
                    item["url"],item["created"] )
                self.character.append(temp)
    
    def listByCreated(self,date):
        result = []
        self.page1 = []
        for item in self.character:
            if item.getCreated() == date and item.getChar_name() not in result:
                result.append(item.getChar_name())
        if len(result) > 20:
            for i in range(0,20):
                self.page1.append(result[0])
                result.remove(result[0])
        for name in self.page1:
            print(name)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for remain in result:
            print(remain)


if __name__ == "__main__":
    test = HandleRequest()
    test.addCharacter()
    test.listByCreated("2017-12-26")
    
