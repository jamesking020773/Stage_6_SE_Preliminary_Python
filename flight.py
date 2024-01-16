class Flight():
    def __init__(self, capacity): 
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():  #using 'not' is eqivalent to 'self.open_seats == 0'
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers) #Total capacity set when the flight instance was created - length of current passenger array


flight = Flight(3) #Creates a flight instance and assigns the capacity variable the value of 3

people = ["Harry", "Ron", "Hermione", "Ginny", "James"]
for person in people:
    if flight.add_passenger(person):
        print(f"{person} was successfully added to the flight.")
    else:
        print(f"No available seat on this flight for {person}")

