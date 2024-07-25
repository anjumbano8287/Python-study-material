# # class Dog:
# #     pass
# # obj = Dog()
# # print(obj)

# # class Dog:

# #     # class attribute
# #     attr1 = "boy"

# #     # Instance attribute
# #     def __init__(self, name):
# #         self.xyz = name

# # Driver code
# # # Object instantiation
# # Rodger = Dog("mukesh")
# # Tommy = Dog("Tommy")

# # Accessing class attributes
# # print("mukesh is a {}".format(Rodger.__class__.attr1))
# # print("Tommy is also a {}".format(Tommy.__class__.attr1))

# # Accessing instance attributes
# # print("My name is {}".format(Rodger.xyz))
# # print("My name is {}".format(Tommy.xyz))

# # class anju:
# #     # studentperforma="i am still a student"
# #     def __init__(simmy,fname,age,address):
# #         simmy.firstname=fname
# #         simmy.Age=age
# #         simmy.Address=address
# #     def speak(self):
# #         print("my name is ",self.firstname,"my age is ",self.Age,"and my address is ",self.Address)
# # obj1=anju("simran",20,"sanjay colony")
# # obj2=anju("anjum",22,"gonchhi")

# # # print("my name is ",obj1.firstname,"my age is ",obj1.Age,"and my address is ",obj1.Address)
# # # print("my name is ",obj2.firstname,"my age is ",obj2.Age,"and my address is ",obj2.Address)
# # print(obj2.__class__.studentperforma)
# # print(obj2.__class__.studentperforma)


# # obj1.speak()
# # obj2.speak()


# # class Pet:
# #     a=10
# # obj1=Pet()    
# # print(obj1.a)
  
# #to print car attributes

# # class Thar:  
# #     def __init__(self,modelname, year):  
# #         self.modelname = modelname  
# #         self.year = year  
# #     def display(self):  
# #         print("this is car:",self.modelname,",","this is year:",self.year)  
  
# # c1 = Thar( "Toyota",2016)
# # c2 = Thar("fortuner",2023)  
# # c1.display() 
# # c2.display()

# # class Thar:  
# #     def __init__(self,modelname, year):  
# #         self.modelname = modelname  
# #         self.year = year  
# #     # def display(self):  
# #     #     print("this is car:",self.modelname,",","this is year:",self.year)  
  
# # c1 = Thar( "Toyota",2016)
# # c2 = Thar("fortuner",2023)  
# # # c1.display() 
# # # c2.display()
# # print("my car is ",c1.modelname,",","my year is ",c1.year)
# # # print("my name is ",c2.modelname,","," my year is ",c2.year)


# # class Pencil:
# #     def __main__(color,shade,HB):
# #         color.shade=shade
# #         color.HB=HB
# # o1=Pencil("blue",2)
# # o2=Pencil("red",5)
# # print("the color of pencil is:",o1.shade,"the quality of pencil:",",",o1.HB)
# # print("the color of pencil is:",o2.shade,"the quality of pencil:",",",o2.HB)


# # class Jar:
# #     y=10
# #     d=20
# #     def func(a):
# #             print(20+30)
# #     def func2(b):
# #             print(50+60)  
# # obj=Jar()
# # obj.y

# # obj.func()
# # obj.func2()

# # class Dog:

# #     # class attribute
# #     # attr1 = "mammal"

# #     # Instance attribute
# #     def __init__(self, name):
# #         self.name = name

# # Driver code
# # Object instantiation
# # Rodger = Dog("Rodger")
# # Tommy = Dog("Tommy")

# # # Accessing class attributes
# # print("Rodger is a {}".format("dog"))
# # print("Tommy is also a {}".format("dog"))

# # # # Accessing instance attributes
# # # print("My name is {}".format(Rodger.name))
# # # print("My name is {}".format(Tommy.name))

     

# # txr1="welcome to {name}   {oo}".format(name="helo",oo="happy",)
# # print(txr1)


# # class student:
# #     institute="letslearncoding"
# #     def __init__(self,name,age,salary):
# #         self.name=name
# #         self.age=age
# #         self.salary=salary
# #     def simmy(self):
# #         print( "my name is", self.name," and my age is ",self.age ,"and my salary is ",self.salary)
# # Anjum=student('Anjum','22','10000')
# # Anjum.simmy()
# # print("Institue name is {}".format(Anjum.__class__.institute))
# # print("My name is {} ".format(Anjum.name),"my age is {}".format(Anjum.age),"and my salary is {}".format(Anjum.salary))
# # print("My name is {}".format(Anjum.age))
# # print("My name is {}".format(Anjum.salary))



class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("My name is {}".format(self.name))
        print(" my class is {}".format(self.age))

# Driver code
# Object instantiation
Rodger = Dog("gimmy",70)
Tommy = Dog("Tommy",60)

# Accessing class methods
Rodger.speak()
Tommy.speak()



# A Python program to demonstrate inheritance
# class Person():
   
#   # Constructor
#   def __init__(simmy, name, id):
#     simmy.name = name
#     simmy.id = id
 
#   # To check if this person is an employee
#   def Display(simmy):
#     print(simmy.name, simmy.id)
 
 
# # Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()

# class Emp(Person):
   
#   def Print(self):
#     print("Emp class called")
     
# Emp_details = Emp("Mayank", 103)
 
# # calling parent class function
# Emp_details.Display()
 
# # Calling child class function
# Emp_details.Print()


# class kite:
#     def __init__(self,color,brand,festive):
#         self.color=color
#         self.brand=brand
#         self.festive=festive
#     def disp(self):
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
#         print("my kite color is:{} 🌀🔷🩷,".format(self.color),"brand name is :{}💣💣💥💥 ,".format(self.brand) ,"on occassion is play kite:{}🪁🪁🪁🪁".format(self.festive))    
        
# king=kite("blue","mapro","janmastmi")
# king1=kite("pink","wipro","15 august")
# king.disp()
# king1.disp()


# hello everyone today we are covering git with github