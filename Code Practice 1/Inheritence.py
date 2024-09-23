class Car1():
    def __init__(self,windows,doors,enginetype):
        self._windows=windows
        self._doors=doors
        self._enginetype=enginetype

class Truck(Car1):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower = horsepower

truck=Truck(4,2,'Diesel',4000)
print(truck)
