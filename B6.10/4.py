class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Guest(Person):
    def __init__(self, name, city, status):
        Person.__init__(self,name, city,)
        self.status = status

    def add_to_list(self, g_list):
        return g_list.append(f'{self.name}, г.{self.city}, статус "{self.status}"')

    def display_guest(self):
        return f'{self.name}, г.{self.city}, статус "{self.status}"'

guests_list = []
guest1 = Guest('Иван Петров', 'Москва', 'Наставник')
guest2 = Guest('Илья Варламов', 'Москва', 'Блогер')
guest1.add_to_list(guests_list)
guest2.add_to_list(guests_list)
print(guest1.display_guest())
print(guests_list)