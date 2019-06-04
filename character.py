class Character():
    def __init__(self,id,name,status,species,type_char,origin,location,image,episode,url,created):
        self.id = id
        self.char_name = name
        self.status = status
        self.species = species
        self.type = type_char
        self.origin = origin
        self.location = location
        self.image_URL = image
        self.episode = episode
        self.url = url
        self.created = created[:10]

    def getId(self):
        return self.id
    
    def getChar_name(self):
        return self.char_name
    
    def getStatus(self):
        return self.status
    
    def getSpecies(self):
        return self.species

    def getType(self):
        return self.type

    def getOrigin(self):
        return self.origin
    
    def getLocation(self):
        return self.location
    
    def getImage_URL(self):
        return self.image_URL

    def getEpisode(self):
        return self.episode
    
    def getURL(self):
        return self.url
    
    def getCreated(self):
        return self.created