class Student:
    def __init__(self, name = "Denis", age = "17", group_number = "2ИСПк-1"):
        self. name = name
        self. age = age
        self. groupnumber = group_number
    def get_name(self):
        return f"имя - {self.name}"
    def get_age(self):
        return f"возраст - {self.age}"
    def get_group_number(self):
        return f"номер группы - {self.groupnumber}"
    def set_name_age(self, name, age):
        self. name = name
        self. age = age
        return f"имя - {self.name}, возраст - {self.age}"
    def set_group_number(self, group_number):
        self. groupNumber = group_number
        return f"группа -{self.groupNumber}"


Yarik = Student('Ярик',18,"2ИСПк")

Artem = Student("Артем", 18, "2ИСПк")
Egor = Student()
Anton = Student()
Beluy = Student("Белый", 18, "2ИСПК")
print(f'{Yarik.get_name()}, {Yarik.get_age()}, {Yarik.get_group_number()}')
print(f'{Artem.get_name()}, {Artem.get_age()}, {Artem.get_group_number()}')
print(f'{Egor.set_name_age("Егор", 17)}, {Egor.set_group_number("1ИСП")}')
print(f'{Anton.set_name_age("Антон", 17)}, {Anton.set_group_number("1ИСП")}')
print(f'{Beluy.get_name()}, {Beluy.get_age()}, {Beluy.get_group_number()}')