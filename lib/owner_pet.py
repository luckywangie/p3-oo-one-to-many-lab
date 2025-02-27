class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet to the all list
        Pet.all.append(self)

        # If an owner is provided, associate the pet with the owner
        if owner:
            owner.add_pet(self)

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # List to hold the owner's pets

    def pets(self):
        # Return a list of pets owned by this owner
        return self._pets

    def add_pet(self, pet):
        # Ensure that the pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception(f"Expected instance of Pet, got {type(pet)}")
        
        # Add the pet to this owner's list of pets
        if pet not in self._pets:
            self._pets.append(pet)
        
        # Add this owner to the pet's owner if not already set
        if pet.owner != self:
            pet.owner = self

    def get_sorted_pets(self):
        # Return a sorted list of pets by their names
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name={self.name})"
