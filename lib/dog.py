#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Troy", breed="Chihuahua"):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Troy" 
        if isinstance(self._name, str) and 1 <= len(self._name) <= 25:
            if breed in APPROVED_BREEDS:
                self._breed = breed
            else:
                print("Breed must be in list of approved breeds.")
                self._breed = "Chihuahua" 
        else:
            self._breed = "Chihuahua" 
      
    def get_name(self):
        print(f"Retriving name")
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)
    
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print(f"Setting breed to {breed}")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.") 

    breed = property(get_breed, set_breed) 
    
   