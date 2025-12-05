class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False
    а

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

# дочерний класс, подкласс
class Bus(Car):
    pass


class Truck(Car):
    def drive_to(self, destination):
        print(f"Truck {self.model} driving to {destination}")

    def test(self):
        print(f"Truck test: {self.model}")