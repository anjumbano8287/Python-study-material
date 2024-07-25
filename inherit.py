# class Parent(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# chaman=Parent("mukesh",70)
# chaman.display()
# # aman=Parent("suresh",40) 
# # chaman.display()
# # aman.display()
# class Child(Parent):
#     def klml(self):
#         print("hii this is inheritance programm")
# aman=Child("suresh",89)  
# aman.klml()
# aman.display()  


# class Manager(object):
#     def __init__(self,name,post):
#         self.name=name
#         self.post=post
#     def getName(self):
#         return self.name
#     def isemployee(self):
#         return False
# elo=Manager("mukesh","assitant")
# print(elo.getName(),elo.isemployee()) 

# class Employee():
#     def notemployee(self):
#         print("true")
# # elo=Manager("mukesh","assitant")
# # print(elo.getName(),elo.isemployee())  

# elo=Employee()
# # print(elo.getName(),elo.notemployee()) 
# elo.notemployee()

# class Aloo:
#     def __init__(self,name):
#         self.name=name
#     def isemployee(self):
#         return False 
# class Chips(Aloo):
#     def isemployee(self):
#         return True
# sabji=Aloo("ramkishan")    
# print("my name is :{}".format(sabji.name))  
# sabji=Chips("mohan das") 
# print("my name is :{}".format(sabji.name))
        
# Python code to demonstrate how parent constructors
# are called.

# parent class
# class Person(object):

#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber

#     # def display(self):
#     #     print(self.name)
#     #     print(self.idnumber)
        
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
    
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post

#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
        
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))


# creation of an object variable or an instance
# a = Person('Rahul', 886012 )

# calling a function of the class Person using
# its instance
# a.display()
# a.details()
# print(a.details())
# print(a.display())



# parent class
class Person():
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
 
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post
    def display2(self):
        print(self.salary)
        print(self.post)
 
        
        
        
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()
a.display2()



