class Vehicle:

    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return 100 * self.seating_capacity
    
class Bus(Vehicle):

    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)
    
    def fare(self):
        second_fare = super().fare()
        maintenance_fee = 0.1 * second_fare
        total_fare = second_fare + maintenance_fee
        return total_fare
bus = Bus()
print(bus.fare())