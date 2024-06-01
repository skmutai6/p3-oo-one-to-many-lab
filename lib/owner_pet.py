class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = 'Farmer' ):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


        if pet_type not in Pet.PET_TYPES:
            raise Exception("Pet type not Valid")


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        pass

    def add_pet(self, pet):
        self.pet = pet
        self.pet.append
        

    def get_sorted_pets(self):
        pass

    


