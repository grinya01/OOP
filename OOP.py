# Наследование
class Animal():

    def __init__(self):
        print("Animal class created")

    def who_am_i(self):
        print("I am an animal")

    def sleep(self):
        print("I am sleeping")


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Cat class created")

    def who_am_i(self):
        print("I am a cat")

    def voice(self):
        print("meow!")


my_animal = Cat() #Cat class created
my_animal.sleep() #I am sleeping


#Абстракция
class Animal:

    def __init__(self, name):
        self.name = name
        print(self.name + " was changed.")

    def just_dog(self):
        print("woof!")


spot = Animal("animal") #animal was changed.
spot.just_dog() #woof!


#Полиморфизм
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF"


class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW"

my_dog = Dog("Sharik")
print(my_dog.speak()) #Sharik says WOOF
my_cat = Cat("Vasya")
print(my_cat.speak()) #Vasya says MEOW


#Инкапсуляция
class Animal:

    def __init__(self):
        self.__size = "big"

    def get_size(self):
        print("I'm a " + self.__size + " animal")

    def set_size(self, new_size):
        self.__size = new_size


animal = Animal()
animal.get_size()  #I'm a big animal

anim = Animal()
anim.set_size("small")
anim.get_size() #I'm a small animal