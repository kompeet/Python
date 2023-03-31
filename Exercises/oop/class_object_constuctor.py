class People:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def my_name(self):
        print("My name is {}".format(self.name))

    def my_age(self):
        print("I am {} years old.".format(self.age))


people1 = People("Jose", 30, "Equador")
people2 = People("Jane", 37, "Belgium")

print(people1.name)
print(people2.country)
people1.my_name()
people2.my_age()



# Inheritance


class Women(People):
    def my_name(self):
        print("My name is {}, and I am a woman".format(self.name))


women1 = Women("Rachel", 25, "Spain")

women1.my_name()
