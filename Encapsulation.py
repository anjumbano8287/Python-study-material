# Python program to 
# demonstrate protected members 
  
# Creating a base class 
# class Base: 
#     def __init__(self): 
  
#         # Protected member 
#         self._a = 2
  
# # Creating a derived class 
# class Derived(Base): 
#     def __init__(self): 
  
#         # Calling constructor of 
#         # Base class 
#         Base.__init__(self) 
#         print("Calling protected member of base class: ",  
#               self._a) 
  
#         # Modify the protected variable: 
#         self._a = 3
#         print("Calling modified protected member outside class: ", 
#               self._a) 
  
  
# obj1 = Derived() 
  
# obj2 = Base() 
  
# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 
  
# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 





# Creating a Base class 
  
  
# class Base: 
#     def __init__(self): 
#         self.a = "GeeksforGeeks"
#         self.__c = "Letslearncoding"
#     def anjum(self):
#         print(f"Anjum is learning at {self.__c} institute")
  
# # Creating a derived class 
# class Derived(Base): 
#     def __init__(self): 
  
#         # Calling constructor of 
#         # Base class 
#         Base.__init__(self) 
#         print("Calling private member of base class: ") 
#         print(self.__c) 
  
  
# # Driver code 
# obj1 = Base() 
# obj1.anjum()
# print(obj1.a) 
# print(obj1.c)

# obj2=Derived()
# import math
# class Circle:
#     def __init__(self,r,name):
#         self.r=r
#         self.name=name
#     def display(self):
#         print(f" the radius of circle is {self.r}")
#         print("the name of the circle is", (self.name))
#     def calculatearea(self):
#         return math.pi*self.r**2
#     def perimeter(self):
#         return 2*math.pi*self.r
# r=int(input("enter the radius "))
# name=input("enter the name") 
# obj=Circle(r,name) 
# print(obj.calculatearea())
# print(obj.perimeter())


# from datetime import datetime
# class parent:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth
#     def calculate_age(self):

# # Import the date class from the datetime module to work with dates
# from datetime import date

# # Define a class called Person to represent a person with a name, country, and date of birth
# class Person:
#     # Initialize the Person object with a name, country, and date of birth
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
    
#     # Calculate the age of the person based on their date of birth
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# # Example usage
# # Create three Person objects with different attributes
# person1 = Person("Ferdi Odilia", "France", date(2022, 7, 20))
# # person2 = Person("Shweta Maddox", "Canada", date(1982, 12, 20))
# # person3 = Person("Elizaveta Tilman", "USA", date(2000, 12, 1))

# # Access and print the attributes and calculated age for each person
# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of_birth)
# print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of_birth)
# print("Age:", person2.calculate_age())

# print("\nPerson 3:")
# print("Name:", person3.name)
# print("Country:", person3.country)
# print("Date of Birth:", person3.date_of_birth)
# print("Age:", person3.calculate_age())


# class calculator:
#     def add(self,x,y):
#         return x+y
#     def sub(self,x,y):
#         return x-y
#     def divide(self,x,y):
#         if y!=0:
#             return x/y
#         else:
#             pass
# x=int(input("enter the first number")) 
# y=int(input("enter the second number")) 
# obj=calculator()      
# print("the sum of numbers id:",obj.add(x,y))
# print("the sub of numbers id:",obj.sub(x,y))
# print("the divide of numbers id:",obj.divide(x,y))



# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,items):
#         self.items.append(items)  
#     def pop 

class bank:
    def __init__(self,name,acnum):
        self.name=name
        self.acnum=acnum
        



  































