### - OOP - use of objects created from classes
# - objects can have their own data (attributes) and behavior (methods)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    # Methods
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

dog1 = Dog("Buddy", 'Golden Retriever')
# run a method of the object:
dog1.bark()  ## out: Buddy says: Woof! Woof!
# retrieve an attribute
print(dog1.name)
dog1.name = "Besty"
print(dog1.name)

dog2 = Dog("Max", "Labrador")


# create a class 
class myclass:
    x = 5

print(MyClass)

# Create object of that class
p1 = myclass() # --> <class '__main__.MyClass'>
print(p1)   # --> <__main__.myclass object at 0x11ad6db10>
print(p1.x)

## All classes have a function called __init__(), which is ALWAYS
# executed when the class is being initiated.
# use the __init__() function to assign values to object properties, 
# or other operariosn necessary to the objet being created. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print ("Instantiating a new Person object:")
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

## What about the __str__() function?
# - it controls what should be returned when the class object is 
# represented as a string.
# If it is not set, the string representation of the object is returned: 

print(p1)  #--> returns: <__main__.Person object at 0x11ada6ad0>

# now if the object has a __str__() function defined: 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

print ("Instantiating a new Person object:")
p1 = Person("Mary", 28)
print(p1)  ## --> Not this returns: Mary (28)


### - Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def printname(self):
        print(self.firstname, self.lastname)

## Now create a child class Student.
#  it will inherit properties and methods from the parent

class Student(Person):
    pass

s1 = Student("Mike", "McGee")
s1.printname()

## Now add an init method to the child class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  # add a new method to the child class
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()
print(x.graduationyear)
x.welcome()