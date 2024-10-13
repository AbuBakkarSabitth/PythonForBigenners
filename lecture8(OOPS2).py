# class Student:
#     def __init__(self,name):
#         self.name=name
# s1 =Student("Shradha")
# print(s1.name)
# del s1.name
# print(s1.name) #Output:AttributeError: 'Student' object has no attribute 'name'





# # #Private(like) attributes & methods
# # #Conceptual Implentations in Python
# # #Private attributes & methods are meant to be used only within the class and are not accessible from outside the classs

# # Abstraction: Hiding the implentation details of a class and only showing the essential features to the user
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started")
# car1=Car()
# car1.start() #self.clutch &self.acc is not showing.so it is called abstraction
# #Encapsulation: Wrapping data and functions into a single unit(onject)
# #Practice:Create Account class with 2 attributes -balance & account no.Create methods for debit,credit & printing the balance
# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no = acc
#     #debit method
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs",amount,"was credited")
#         print("total balance= ",self.get_balance())
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs. ",amount,"was credited")
#         print("total balance = ",self.get_balance())
#     def get_balance(self):
#         return self.balance    





# acc1=Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no)

# acc1.debit(1000)
# acc1.credit(1000)
#DEL KEYWORD

# class Student:
#     def __init__(self,name):
#         self.name=name
# s1 = Student("Sabith")
# print(s1.name)
# del s1.name
# print(s1.name) #'Student' object has no attribute 'name'
#Private(like) attributes & methods
#Private attributes & methods are meant to be used only within the class and are not accessible from outside the class
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
    
# acc1 = Account("12345","abcde")
# # print(acc1.__acc_pass)
# print(acc1.reset_pass()) #So we can see private attribute by this way



# class Person:
#     __name= "anonymous"
    
#     def __hello(self,name):
#         print("hello person!")
        
#     def welcome(self):
#         self.__hello(self.__name)
#         return self.__name; #Accessing the private variable


# p1 = Person()
# print(p1.welcome())



#Inheritance : When one class(child/derived) derives the properties & methods of another class(parent/base)
# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class ToyotoCar(Car):
#     def __init__(self,name):
#         self.name=name
        
# car1 =ToyotoCar("fortuner")
# car2= ToyotoCar("prous")

# print(car1.name)

# print(car1.start())#it al
# print(car1.color)



#Inheritance
#Types: #single,Multi-level,Multiple

#Single Inheritance
#Multi-level Inheritance
#Muliple Inheritance



#Multi-level Inheritance
# class Car:
#     @staticmethod
#     def  start():
#         print("car started...")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,type):
#         self.type=type
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type
# car1= Fortuner("dissel")
# car1.start()  #It's working


#Multiple Inheritance

# class A:
#     varA="welcome to class  A"
# class B:
#     varB="wellcome to class B"
# class C(A,B):
#     varC ="welcome to class C"
# c1= C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


#Super method: is used to access method of the  parent class

# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
    
# class ToyotaCar(Car):
#     def __init__(self,name,type):

#         self.name=name
#         super().__init__(type)
#         super().start()


# #We can also parent's class method by super()
# car1=ToyotaCar("peitus","electric")
# print(car1.type)



#Class method
#A class method is bound to the class & receives the class as an implicit first argument
# class Person:
    # name="anonymous"
    # def changeName(self,name):
    #     Person.name=name
# #or,
#     def changeName(self,name):
#         self.__class__.name="Rahul"

#     @classmethod
#     def changeName(cls,name):
#         cls.name= name;


# p1=Person()
# p1.changeName("Sabith")
# print(p1.name)
# print(Person.name)


#static method

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     #     self.percentage=str((self.phy+self.chem+self.math)/3) +"%"
#     # def calcPercentage(self):
#     #     self.percentage=str((self.phy+self.chem+self.math)/3) +"%"

#     @property
#     #We use @property decorator or any method in the class  to use the method as a property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"


# stu1=Student(98,98,98)
# print(stu1.percentage)
# stu1.phy= 87

# print(stu1.phy)
# # print(stu1.percentage)
# # stu1.calcPercentage()
# print(stu1.percentage)


#Polymerphism:   When the same operator is allowed to have different meaning  according to the context
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def showNumber(self):
#         print(self.real,"i +" ,self.img,"j")
    # def add(self, num2):
    #     newReal = self.real +num2.real
    #     newImg= self.img + num2.img
    #     return Complex(newReal,newImg)
#     def __add__(self, num2):
#         newReal = self.real +num2.real
#         newImg= self.img + num2.img
#         return Complex(newReal,newImg)
# num1 =Complex(1,3)
# num1.showNumber()
# num2 = Complex(23,43)
# num2.showNumber()

# # num3 =num1.add(num2)
# num3=num1+num2
# num3.showNumber()

#Qs.Define a Circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the circle
#Define a Perimeter() methd of the class which allows you to calculate the  perimeter of the circle
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return (22/7) * self.radius **2
#     def perimeter(self):
#         return 2*(22/7)*self.radius
# c1=Circle(21)
# print(c1.area())
# print(c1.perimeter())


#Define a Employee class with attributes role,department &salary.This class also showDetails() method
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#     def showDetails(self):
#         print("Role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)

# e1=Employee("accountant","Finance","50,444")
# e1.showDetails()
#Create an Engineeer class that inherits properties from Employee  & has additional attributes: name & age
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#     def showDetails(self):
#         print("Role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT","75,443")

# engg1=Engineer("Tahil",44)
# engg1.showDetails()

#CREATE a class called Order which stores item & its price.Use Dunder function__gt__() to convey that: order1>order2 if price of order1>price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr22):
        return self.price>odr22.price
    
odr1 =Order("chips",40)
odr2=Order("Juice",32)
print(odr1>odr2) #true

