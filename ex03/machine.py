import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.coffee_served = 0
        self.broken = False

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
        
    def repair(self):
        if self.broken == False:
            return
        self.broken = False

    def serve(self, bev_der):
        coin = random.randint(0, 1)
        if self.broken : 
            raise self.BrokenMachineException()
        self.coffee_served += 1
        print(f"Coffee served: {self.coffee_served}")
        print(f"Machine broken: {self.broken}")
        if self.coffee_served % 10 == 0:
            self.broken = True
        if coin == 0:
            return self.EmptyCup()
        else :
            return bev_der()
        
def main():
    machine = CoffeeMachine()
    drinks = [Coffee, Tea, Chocolate, Cappuccino]

    drink = random.choice(drinks)
    for d in range(2):
        for e in range (15):
            try:
                bev = machine.serve(drink)
                print(bev)
            except machine.BrokenMachineException as e:
                print(e)
        machine.repair()

if __name__ == "__main__":
    main()