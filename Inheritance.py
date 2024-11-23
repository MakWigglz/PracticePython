class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

  def print_info(self):
      print(f'{self.name is {self.age} years old')


# Child Class
# Name of the parent class in the definition of the child class
# Constructor of the parent class called within the constructor of the child class

class Person:
  def __init__(self, name, age):
       self.name = name
       self.age = age
  def print_info(self):  
      print(self.name)
      print(self.age)

class Teacher(Person):    
   def __init__(self, name, subject):
      self.subject = subject
      Person.__init__(self, name, age)

# Instance of the child class Teacher, of the parent class Person:

myTeacher = Teacher("Dr. Hirani", 49, "computer science")
myTeacher.print_info()
print(myTeacher.subject)

# Output: 
    Dr. Hirani
    49
    computer science



   
 

 
    





