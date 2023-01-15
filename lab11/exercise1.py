class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name): self.__name = name
    def set_number(self, number): self.__number = number
    def get_name(self): return self.__name
    def get_number(self): return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, wage):
        super().__init__(name, number)
        self.__shift = shift
        self.__wage = wage
    
    def set_shift(self, shift): self.__shift = shift
    def set_wage(self, wage): self.__wage = wage
    def get_shift(self): return self.__shift
    def get_wage(self): return self.__wage

def main():
    worker = ProductionWorker(input("name: "), input("employee number: "), int(input("shift (1 or 2): ")), float(input("wage: ")))
    print(worker.get_name(), worker.get_number(), "day" if worker.get_shift() == 1 else  
        "night" if worker.get_shift() == 2 else "unknown", worker.get_wage())

if __name__ == "__main__":
    main()

    