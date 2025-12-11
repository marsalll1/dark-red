class Animal:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, new_age: int) -> None:
        self.__age = new_age

    def make_sound(self) -> str:
        raise NotImplementedError("Subclasses must implement make_sound().")


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"



if __name__ == "__main__":
    dog = Dog("Buddy", 3)
    cat = Cat("Luna", 2)

    print(dog.get_name(), dog.get_age(), dog.make_sound())
    print(cat.get_name(), cat.get_age(), cat.make_sound())

    dog.set_name("Rex")
    dog.set_age(4)
    cat.set_name("Mila")
    cat.set_age(3)

    print(dog.get_name(), dog.get_age())
    print(cat.get_name(), cat.get_age())
