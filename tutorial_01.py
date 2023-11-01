

def print_my_name(name):
    print(name)

# Parent class / super class / base class
class Device:
    def __init__(self, type, color, size) -> None:
        self.type = type
        self.color = color
        self.size = size

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

class Equipment:
    def __init__(self, type, color, size) -> None:
        self.type = type
        self.color = color
        self.size = size
        self.weight = 50

# Child / subclass
class Phone(Device):
    pass

# Child /subclass
class Computer(Device):
    def __init__(self, type, color, size, ports):
        self.ports = ports
        super().__init__(type, color, size)
    
    def set_color(self, color):
        print("Computer Class: ", self.color)
        super().set_color(color)

if __name__ == "__main__":
    # phone 1
    phone_1 = Phone("iphone 13 pro max", "black", 6.7)
    print(phone_1.color)
    print(phone_1.type)
    print(phone_1.size)
    phone_1.set_color("red")
    print(phone_1.color)

    # phone 2
    phone_2 = Phone("Samsong", "blue", 5.1)
    print(phone_2.color)
    print(phone_2.type)
    print(phone_2.size)

    # computer 1
    computer_1 = Computer("HP Elite", "Gray", 14, "USB-C")
    print("Computer 1 color: ",computer_1.color)
    print("Computer 1 color: ",computer_1.ports)
    computer_1.set_color("red")
    print("Computer 1 color: ",computer_1.color)
