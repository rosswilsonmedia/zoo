class Animal:
    def __init__(self, name, type, age):
        self.name=name
        self.type=type
        self.age=age
        self.health=100
        self.happiness=100
    def feed(self):
        self.health+=10
        self.happiness+=10
        return self
    def display_info(self):
        print(f"{self.name}\n{self.type}\nHealth: {self.health}\nHappiness: {self.happiness}\n")

class Lion(Animal):
    def __init__(self, name, age):
        self.name=name
        self.type='Lion'
        self.age=age
        self.health=80
        self.happiness=80
    def feed(self):
        self.health+=5
        self.happiness+=2
        return self
class Tiger(Animal):
    def __init__(self, name, age):
        self.name=name
        self.type='Tiger'
        self.age=age
        self.health=100
        self.happiness=85
    def feed(self):
        self.health+=5
        self.happiness+=3
        return self
class Bear(Animal):
    def __init__(self, name, age):
        self.name=name
        self.type='Bear'
        self.age=age
        self.health=90
        self.happiness=50
    def feed(self):
        self.health+=10
        self.happiness+=5
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, name, type, age):
        self.animals.append( Animal(name, type, age) )
    def add_lion(self, name, age):
        self.animals.append( Lion(name, age) )
    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age) )
    def add_bear(self, name, age):
        self.animals.append( Bear(name, age) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def feed_animals(self):
        for animal in self.animals:
            animal.feed()
        return self
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 2.5)
zoo1.add_lion("Simba", 2.5)
zoo1.add_tiger("Rajah", 37)
zoo1.add_tiger("Shere Khan", 38)
zoo1.add_bear('Baloo',35)
zoo1.feed_animals()
zoo1.print_all_info()