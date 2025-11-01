class Vehicle:

    def __init__(self, name, mileage, speed):
        self.name = name
        self.mileage = mileage
        self.speed = speed

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 30, 120 )
print("The school bus' name is {}".format (school_bus.name))
print("The school bus' mileage is {}".format (school_bus.mileage))
print("The school bus' speed is {}".format (school_bus.speed))