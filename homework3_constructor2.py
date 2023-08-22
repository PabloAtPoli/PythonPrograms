
class Horse:
    def __init__(self, name, age, color = "white", rider = "John"):
        self.name = name
        self.age = age
        self.color = color
        self.rider = rider
      
    
    def print(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Color: ", self.color)
        print("Rider: ", self.rider)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}, Rider: {self.rider}"
        
    
horse = Horse(name = "Django", age=5, color="Brown", rider="Pablo")
print(horse)

print("Horse dictionary:")
print(horse.__dict__)

print(type(horse))
      