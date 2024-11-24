# #uzyj slownik, stwórz forularz używając funkcji input w którym bede pytać użytkownika o:
# #imie, nazwisko, wiek, miejsce urodzenia, wzrost, girth, length, 
# #i zapisz to wszystko w słowniku <


# form = {
#     "name" : "ass",
#     "last name" : "cheeks",
#     "age" : 21,
#     "place of birth" : "Sosno",
#     "height" : 3,
#     "girth" : 21,
#     "length" : 5000
# }

# form["name"] = input("name: \n")

# #print(form["name"])

# form["last name"] = input("last name: \n")
# form["age"] = input("age: \n")
# form["place of birth"] = input("place of birth: \n")
# form["height"] = input("height: \n")
# form["girth"] = input("girth: \n")
# form["length"] = input("length: \n")

# print(form)

#----------LESSON 1 CHAPTER 2 ----------------------- 
#importuje jsona 
# import json

# form = {
#     "name" : "ass",
#     "last name" : "cheeks",
#     "age" : 21,
#     "place of birth" : "Sosno",
#     "height" : 3,
#     "girth" : 21,
#     "length" : 5000
# }

# file_name = "Jason.json" 
# with open(file_name, "w") as obj:
#     json.dump(form, obj)
    
#zrob klase 
class Capybara():
    def __init__(self, name, age): # <-- Trzeba zainicjalizować zanim możemy skorzystać z metod klasy
        self.name = name
        self.age = age

    def chill(self):
        print("snor snor")

    def greetings_mortals(self): #<to metoda
        print(f"My glorious name is {self.name}. Bow before me or perish!")

capi = Capybara ("Kapec", 22)
print(capi)

capi.greetings_mortals()
capi.chill()


#homework : klasa, ktora bedzie przyjmowac dane, metode export, ktora bedzie eksportowala dane do json 
#te dane maja byc w slowniku MAM selfa zamienic na slownik albo stworzyc slownik w metodzie w klasie
#metoda to funkcja w klasie
#jak to zrobie to zmienic klase zeby mogla przyjmowac dane pisane recznie albo sciezke do pliku w tym pliku i z tego 
#dane z jsona maja byc w klasie

# import json

# class Data():
#     def __init__(self, name=None, age=None, file_name=None): 
#         self.name = name
#         self.age = age
#         self.file_name = "my_export.json"

#     def elongated_data(self):
#         print(f"name: {self.name}\nage: {self.age}")

#     def export(self):
#         with open(self.file_name, "w") as obj:
#             obj.write

import json

class Data:
    def __init__(self, name=None, age=None, file_name="my_export.json"):
        self.name = name
        self.age = age
        self.file_name = file_name

        try:
            self.load_from_file()
        except FileNotFoundError:
            self.export()

    def elongated_data(self):
        print(f"name: {self.name}\nage: {self.age}")

    def export(self):
        with open(self.file_name, "w") as file:
            json.dump({"name": self.name, "age": self.age}, file, indent=4)

    def load_from_file(self):
        with open(self.file_name, "r") as file:
            data = json.load(file)
            self.name = data.get("name", self.name)
            self.age = data.get("age", self.age)

#jakby ktos nie sprawdzil, czy te wartosci z klasy sa puste to moze nam ktos zjebac
kutas = Data(file_name="kutas.json")

kutas.elongated_data()

drugi_kutas = Data()












