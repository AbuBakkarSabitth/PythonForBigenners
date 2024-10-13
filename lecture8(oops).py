# # # # a=10
# # # # b=20


# # # # class Car:
# # # #     color="blue"

# # # # car1=Car()
# # # # print(car1.color)


# # class Student:
# #     college_name="CDA COllege"#class_attribute



# #     def __init__(self): # default parametirezed constructor
# #         pass;

# #     #paramaterize constructor
# #     def __init__(self,fullname,marks):
# #         self.marks=marks#obj_attribute
# #         #obj_attribute>class_attribute
    
# #         self.name=fullname
    
# #         print("adding new student in Database..")
    
# #     def hello(self):
# #         print("welcome student,",self.name) 
# #     def get_marks(self):
# #         return self.marks   

# # s1= Student("karan",34)
# # s1.hello();
# #  #karan
# # # s2=Student("arjun",45)
# # # print(s2.name,s2.marks) #sabith
# # # print(s1.college_name)
# # # print(s2.college_name)
# # print(s1.get_marks())

# # #Class & Instance Attributes

# #Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average
# class Student:
   
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod    
#     def hello():
#         print("hello")
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is:",sum/3)


# s1 = Student("tony stark", [99,43,73])
# s1.get_avg()
# s1.name="iron men"
# s1.get_avg()
# s1.hello()

