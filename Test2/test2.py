class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, type_food, time):
        print(f"{self.name} eats {type_food} for {time} time")

    def run(self, duration):
        print(f"{self.name} runs for {duration} time")

    def show(self):
        print(f"Animal: {self.name}, Age: {self.age}, Color: {self.color}")

class Burung(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def fly(self, high):
        print(f"{self.name} flies {high} high")

    def sleep(self, time):
        print(f"{self.name} sleeps for {time} time")

    def sound(self):
        print(f"{self.name} makes a chirping sound")


burung = Burung("Boddy", 18, "Red")
burung.show()
burung.fly("high")
burung.sleep("8 hours")
burung.sound()
burung.eat("worms", "10 minutes")
burung.run("10 minutes")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self, duration):
        print(f"{self.name} is running for {duration} seconds")

    def fly(self):
        print(f"{self.name} can't fly")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self):
        print("Meuw Meuw")

    def play(self):
        print(f"{self.name} likes to run")


kitty = Cat("Kitty", 2)


kitty.sound()
kitty.eat()
kitty.sleep()
kitty.run(10)
kitty.fly()
kitty.play()

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self, time):
        print(f"{self.name} is sleeping for {time} hours.")

    def sound(self):
        print(f"{self.name} makes a sound.")

    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print("Dog can't fly.")

    def run(self, duration):
        print(f"{self.name} is running for {duration} minutes.")

    def play(self):
        print(f"{self.name} likes to run.")

# Create a Dog object
doggy = Dog("Doggy", 3)


doggy.sleep(8)
doggy.sound()
doggy.show()
doggy.fly()
doggy.run(30)
doggy.play()

class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        return "Bird can fly."

    def sound(self):
        return "Kiew Kiew."

    def run(self, duration):
        return "Display duration"

    def play(self):
        return "Bird doesn't like to run."


birdy = Bird("Birdy", 5)
print(birdy.name)
print(birdy.age)
print(birdy.fly())
print(birdy.sound())
print(birdy.run(10))
print(birdy.play())