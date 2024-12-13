class Manufacturer:
    def __init__(self,identity,location):
        self.__identity = identity
        self.__location = location
    def describe(self):
        print(f"Indentity: {self.__identity} - Location: {self.__location}")

class Device:
    def __init__(self, name, price, identity, location):
        self.__name = name
        self.__price = price
        self.__manufacturer = Manufacturer(identity, location)

    def describe(self):
        print(f"Name: {self.__name} - Price: {self.__price}")
        self.__manufacturer.describe()

device1 = Device("mouse", 2.5, 9725, "Vietnam")
device2 = Device("monitor", 12.5, 11, "Germany")
device1.describe()
device2.describe()