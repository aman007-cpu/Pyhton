class Train:
    def __init__(self,name, fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
    def fareInfo(self):
        print(f"fare of the train is {self.fare}")


romi = Train("Intra",2000,10)
romi.getstatus()
romi.fareInfo()
            