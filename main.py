# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
    def make_sound(self):
        print(f"{self.name} make a sound 'kar-kar'")
    def eat(self):
        print(f"{self.name} eat {self.food}")

class Mammal(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
    def make_sound(self):
        print(f"{self.name} make a sound 'be-e-e!'")
    def eat(self):
        print(f"{self.name} eat {self.food}")

class Reptile(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
    def make_sound(self):
        print(f"{self.name} make no sound")
    def eat(self):
        print(f"{self.name} eat {self.food}")

class Zoo:
    def __init__(self):
        self.animals = animals
        self.employee = employee
    def add_employee(self, new_employee):
        employee.append(new_employee)
    def add_animal(self, new_animal):
        animals.append(new_animal)

class ZooKeeper:
    def __init__(self, name):
        self.name = name
    def feed_animal(self, which_animal):
        print(animals[which_animal].name, "was fed by", self.name, "with", animals[which_animal].food)

class Veterinarian:
    def __init__(self, name):
        self.name = name
    def heal_animal(self, which_animal):
        print(animals[which_animal].name, "was healed by", self.name)


employee = []
#animals = [Reptile("Snake", 10, "mice"), Mammal("Sheep", 1, "grass"), Bird("Crow", 105, "porridge")]
animals = []
Z1 = Zoo()

#employee = [Veterinarian("Joane"), ZooKeeper("Alex")]
with open('our_zoo.txt', 'r') as file:
    for line in file:
        data = line.strip("\n").split()
        wht_clss = data[0]
        name = data[1]
        if wht_clss == "Veterinarian":
            nnemp = Veterinarian(name)
            Z1.add_employee(nnemp)
        elif wht_clss == "ZooKeeper":
            nnemp = ZooKeeper(name)
            Z1.add_employee(nnemp)
        else:
            age = data[2]
            food = data[3]
            if wht_clss == "Reptile":
                nnemp = Reptile(name, age, food)
                Z1.add_animal(nnemp)
            elif wht_clss == "Mammal":
                nnemp = Mammal(name, age, food)
                Z1.add_animal(nnemp)
            elif wht_clss == "Bird":
                nnemp = Bird(name, age, food)
                Z1.add_animal(nnemp)




def animal_sound(animals):
    for i in animals:
        i.make_sound()

animal_sound(animals)

print("")
employee[1].feed_animal(1)
employee[0].heal_animal(2)
employee[1].feed_animal(0)

print("\na new person and a new animal were added, let's see what they do:")
#new_emp = ZooKeeper("Barbara")
new_anim = Bird("Pigeon", 2, "sunflower_grains")


Z1.add_animal(new_anim)
#Z1.add_employee(new_emp)

employee[2].feed_animal(3)


with open('our_zoo.txt', 'w') as file:
    for i in range(len(employee)):
        t = str(type(employee[i]))
        f = employee[i].name
        if t == "<class '__main__.Veterinarian'>":
            t = "Veterinarian"
        elif t == "<class '__main__.ZooKeeper'>":
            t = "ZooKeeper"
        file.write(t + " " + f + "\n")
    for j in range(len(animals)):
        y = str(type(animals[j]))
        n = animals[j].name
        a = str(animals[j].age)
        d = animals[j].food
        if y == "<class '__main__.Reptile'>":
            y = "Reptile"
        elif y == "<class '__main__.Mammal'>":
            y = "Mammal"
        elif y == "<class '__main__.Bird'>":
            y = "Bird"
        file.write(y + " " + n + " " + a + " " + d +"\n")