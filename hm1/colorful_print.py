from blessed import Terminal
from homework1 import Person

term = Terminal()

fruits = {
    "🍎": term.red,
    "🍌": term.yellow,
    "🍇": term.magenta,
    "🍊": term.yellow,
    "🍓": term.red,
    "🍋": term.yellow,
    "🫐": term.blue,
}

for emoji, color_func in fruits.items():
    text = "Это вкусный фрукт!"
    colored_text = color_func(text) + term.normal
    print(f"{emoji} {colored_text}")

person1 = Person("Диана", "10.02.1999", "дизайнер", True)
person2 = Person("Нурсултан", "25.09.1997", "программист", False)
person3 = Person("Сайкал", "14.03.2002", "врач", True)
person = [person1, person2, person3]
for i in person:
    print(i.introduce())

#ЧТОБЫ ПОЛУЧИТЬ ЦВЕТА НАЖМИ ЭТОТ КОММАНДУ:python hm1/colorful_print.py
