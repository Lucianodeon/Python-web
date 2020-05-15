class Flight:
    """docstring for ."""
    counter 1
    def __init__(self, origin, destination, duration):
        self.id=Flight.counter
        Flight.counter += 1

        self.passengers=[]

        #details about de Flight
        self.origin=origin
        self.destination=destination
        self.duration=duration
    def print_info(self):
        print(f"Flight origin:{self.origin}")
        print(f"Flight destination;{self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers")
        for passengers in self.passengers:
            print(f"{passenger.name}")

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id=self.id

    def delay(self,amount):
        self.duration += amount

class Passenger(object):
    """docstring forPassenger."""

    def __init__(self, name):

        self.name = name
def main():
    #create flight.
    f1=Flight(origin="New York", destination="Paris", duration=540)

    #create passengers.
    alice= Passenger(name="Alice")
    bob=Passenger(name="bob")

    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()

if __name__=='__main__'
    main() #calls the function, and only calls it if i access not if I import it
