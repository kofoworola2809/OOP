# Parent idea: different vehicles with same method move()

class Car:
    def move(self):
        return "The car is moving 🚗"
    
class Boat:
    def move(self):
        return "The boat is sailing ⛵"
    
class Plane:
    def move(self):
        return "The plane is flying ✈️"


# Polymorphism in action!
for vehicle in (Car(), Boat(), Plane()):
    print(vehicle.move())

    

