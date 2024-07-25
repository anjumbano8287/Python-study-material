
# abc = "LetsLearnCoding"
# print(len(abc))



# len() being used for a list
# print(len([10, 20, 30]))

# def add(x, y, z = 10): 
#     return x + y+z

# # Driver code 
# print(add(2, 3))
# print(add(2, 3, 4))

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")

#     def language(self):
#         print("Hindi is the most widely spoken language of India.")

#     def type(self):
#         print("India is a developing country.")

# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")

#     def language(self):
#         print("English is the primary language of USA.")

#     def type(self):
#         print("USA is a developed country.")

# obj_ind = India()
# obj_ind.capital()
# obj_usa = USA()
# obj_usa.language()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# Function to take multiple arguments 
# def add(datatype, *args): 
   
#     # if datatype is int 
#     # initialize answer as 0 
#     if datatype =='int': 
#         answer = 0
           
#     # if datatype is str 
#     # initialize answer as '' 
#     if datatype =='str': 
#         answer ='' 
   
#     # Traverse through the arguments 
#     for x in args: 
   
#         # This will do addition if the  
#         # arguments are int. Or concatenation  
#         # if the arguments are str 
#         answer = answer + x 
   
#     print(answer) 
   
# # Integer 
# add('int', 5, 6,7) 
   
# # String 
# add('str', 'Hi ', 'Geeks') 



# class Bird:
#   def intro(self):
#     print("There are many types of birds.")
    
#   def flight(self):
#     print("Most of the birds can fly but some cannot.")
  
# class sparrow(Bird):
#   def flight(self):
#     print("Sparrows can fly.")
    
# class ostrich(Bird):
#   def flight(self):
#     print("Ostriches cannot fly.")
    
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()


# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# # Create a list of Animal objects
# animals = [Dog(), Cat()]

# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())


# class Vehical:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def show(self):
#         print("details:",self.name,self.color)  
#     def speed(self):
#         print("vehical speed max speed is 200")     
# class Car(Vehical):
#     def speed(self):
#         print("car max speed is 100")
# inspector=Car("toyoto","green")
# inspector.show()
# inspector.speed()

# Gadhi=Vehical("wegnar","black")
# Gadhi.speed()
# Gadhi.show()




# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")

#     def language(self):
#         print("Hindi is the most widely spoken language of India.")

#     def type(self):
#         print("India is a developing country.")

# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")

#     def language(self):
#         print("English is the primary language of USA.")

#     def type(self):
#         print("USA is a developed country.")

# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()