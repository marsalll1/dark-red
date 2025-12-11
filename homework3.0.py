from datetime import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, value):
        self.__occupation = value

    @property
    def higher_education(self):
        return self.__higher_education

    @higher_education.setter
    def higher_education(self, value):
        self.__higher_education = value

    @property
    def age(self):
        today = datetime.today()
        years = today.year - self.__birth_date.year
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            years -= 1
        return years

    def introduce(self):
        edu_text = (
            "есть высшее образование"
            if self.__higher_education else
            "высшего образования нет"
        )
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.__occupation}. "
            f"У меня {edu_text}."
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu_text = (
            "есть высшее образование"
            if self.higher_education else
            "высшего образования нет"
        )
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился с Айсулуу в группе {self.group_name}. "
            f"У меня {edu_text}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = (
            "есть высшее образование"
            if self.higher_education else
            "высшего образования нет"
        )
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Мое хобби {self.hobby}. "
            f"У меня {edu_text}."
        )


