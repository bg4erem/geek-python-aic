class Worker:
    name: str
    surname: str
    position: str
    __income = dict()

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        print("Worker created")

    def get_full_name(self):
        print(f"Full name is {self.name} {self.surname}")


class Position(Worker):
    wage: int
    bonus: int

    def __init__(self, wage, bonus, name, surname, position):
        super().__init__(name, surname, position)
        self.wage = wage
        self.bonus = bonus

    def get_total_income(self):
        __income = {'wage' : self.wage, 'bonus' : self.bonus}
        print(sum(__income.values()))


andrew = Position(35000,100000, "Andrew", "Cheremkin", "Manager")
andrew.get_full_name()
andrew.get_total_income()