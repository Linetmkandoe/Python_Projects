# class Vehicle:
#     def__init__(self,make,color):
#         self.make=make
#         self.color=color
#     def accelarate(self):
#         print("Accelaration")

# class Bus:
#     def__init__(self,make,color,passengers):
#     super().__init__(make,def hoot(self)):
#     sel.passengers = passengers
#     def start_boarding(self):
#         print("The bus is boarding")
# class Lorry:
#     def__init__(self,make,color,max_load):
#     super().__init__(make,color)
#     self.max_load = max_load
#     def unload(self):
#         print("unloading")


class Vehicle:
    def __init__(self,make,color):
        self.make=make
        self.color=color
    def accelerate(self):
        print("Accelarate start")
    def hoot(self):
        print("Honk honk")
class Bus(Vehicle):
    def __init__(self, make, color,passenger):
        super().__init__(make, color)
        self.passenger=passenger
    def start_boarding(self):
        print("The bus is boarding")
class Lorry(Vehicle):
    def __init__(self, make, color,max_load):
        super().__init__(make, color)
        self.max_load=max_load
def unload(self):
    print("Unload")



    
