# from abc import ABC, abstractmethod

# class Polygon(ABC):

#     @abstractmethod
#     def noofsides(self):
#         pass


# class Triangle(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")


# class Pentagon(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")


# class Hexagon(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")


# class Quadrilateral(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")


# # Driver code
# R = Triangle()
# R.noofsides()

# K = Quadrilateral()
# K.noofsides()

# R = Pentagon()
# R.noofsides()

# K = Hexagon()
# K.noofsides()


# Python program showing
# abstract base class work
# from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass

# class Human(Animal):

#     def move(self):
#         print("I can walk and run")

# class Snake(Animal):

#     def move(self):
#         print("I can crawl")

# class Dog(Animal):

#     def move(self):
#         print("I can bark")

# class Lion(Animal):

#     def move(self):
#         print("I can roar")

# # Driver code
# R = Human()
# R.move()

# K = Snake()
# K.move()

# R = Dog()
# R.move()

# K = Lion()
# K.move()


# import abc

# class parent:       
#     def geeks(self):
#         pass

# class child(parent):
#     def geeks(self):
#         print("child class")

# # Driver code
# # print( issubclass(child, parent))
# # print( isinstance(child(), parent))
# xyz = child()
# abc = parent()
# abc.geeks()
# xyz.geeks()

# from abc import ABC 
# class Cofee(ABC):
#     # @abstractmethod
#     def drink(self):
#         print("the is addictive drink ")
# class Chaii(Cofee):
#     def drink(self):
#         print("this is also addictive drink")
# class Pepsi(Cofee):
#     def drink(self):
#         print("this is good in hot days")
# class Lassi(Cofee):
#     def drink(self):
#         print("this is fantastic for our health")
# k=Cofee()
# k.drink()

# J=Chaii()
# J.drink()

# l=Pepsi()
# l.drink()
# n=int(input("enter the number"))
# for i in range(1,11):
#     i*=n
#     print(i)

