class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "высшего образования нет"
        return f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, {edu_text}."

person1 = Person("Диана", "10.02.1999", "дизайнер", True)
person2 = Person("Нурсултан", "25.09.1997", "программист", False)
person3 = Person("Сайкал", "14.03.2002", "врач", True)
people = [person1, person2, person3]

for p in people:
    print("Имя:", p.name)
    print("Дата рождения:", p.birth_date)
    print("Профессия:", p.occupation)
    print("Высшее образование:", p.higher_education)
    print(p.introduce())
    print("-" * 40)
