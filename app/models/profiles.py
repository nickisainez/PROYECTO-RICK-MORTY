
class Personaje:
    def __init__(self,id,name,species,status,gender,origin,location,image,created):
        self.id = id
        self.name = name
        self.status = species
        self.species = status
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.created = created
    
    def to_json(self):
        return{
        "id": self.id,
        "name" : self.name,
        "status" : self.species,
        "species" : self.status,
        "gender" : self.gender, 
        "origin" : self.origin,
        "location" : self.location,
        "image" : self.image,
        "created" : self.created
        }