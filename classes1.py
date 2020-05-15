class Flight:
    """docstring for ."""

    def __init__(self, origin, destination, duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

def main():
    #create a Flight
    f=Flight(origin="New York",destination="Paris",duration=548)

    #Change duration
    f.duration+=10 #delay

    #print details about Flight
    print(f.origin)
    print(f.destination)
    print(f.duration)


if __name__=='__main__'
    main() #calls the function, and only calls it if i access not if I import it
