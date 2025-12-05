class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, "
              f"я работаю {self.profession}.")


class Classmate(Person):
    def __init__(self, name, age, profession, group_name):
        super().__init__(name, age, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет! Я {self.name}, учусь в группе {self.group_name}. "
              f"Мне {self.age} лет и я обучаюсь по профессии: {self.profession}.")


class Friend(Person):
    def __init__(self, name, age, profession, hobby):
        super().__init__(name, age, profession)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет! Я {self.name}, мне {self.age} лет. "
              f"Мое хобби — {self.hobby}. Я работаю {self.profession}.")


class BestFriend(Friend):
    def __init__(self, name, age, profession, hobby, shared_memory):
        super().__init__(name, age, profession, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Наше лучшее воспоминание: {self.shared_memory}")


classmate1 = Classmate("Бектур", 20, "студент-программист", "PY-41")
classmate2 = Classmate("Айпери", 19, "дизайнер", "DS-19")

friend1 = Friend("Алмаз", 22, "инженер", "футбол")
friend2 = Friend("Айдар", 23, "повар", "шахматы")

best_friend = BestFriend("Байэл", 21, "разработчик", "игра в шахматы",
                         "как мы выиграли турнир")


print("=== Базовое задание ===")
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

print("\n=== BestFriend ===")
best_friend.introduce()

print("\n=== Доп. задание: список объектов ===")
people = [classmate1, classmate2, friend1, friend2, best_friend]

for person in people:
    person.introduce()
