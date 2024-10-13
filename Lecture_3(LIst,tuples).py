# marks1=94.4
# marks2=87.5
# marks3=95.2
# marks4=66.4
# marks5=45.1
 



# marks=[95.5,85.7,95.5,66.4,45.1];
# print(marks)

# print(type(marks))


# print(marks[0])
# print(marks[1])
# print(len(marks))



# I can inside different types in sets
# student=["karan",34.3,17,"delhi"]
# print(student)
# String is immutable
# Lists is mutable.I mean Changable

# str="hello"
# print(str[0])
# str[0]="y"

# Above codes are error

# student[0]="arjub"
# print(student)

# From above codes,I can change value by using sets

# List Slicing
# marks=[87,64,33,95]
# print(marks[1:4])

# We can slice by negative index
# print(marks[-3:-1])

# list=[2,1,3]
# print(list.sort()) 
# list.append(32)
# print(list)
# list.sort(reverse=True)
# print(list)
# list=['a','d','e','f','c','b']
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.insert(3,4)


# list.pop(2)
# pop(2)  mean it removes the value of the 2th index
# print(list)

# Tupple is immutable
# tup=(2,1,3,1)
# print(tup[0])
# print(tup[1])
# tup[0]=5
# tup[0] is not allowed in python
# print(tup[1:3])
# tup=("sabith",)
# print(tup)
# print(type(tup))

# tup=(1,3,2,2,2)
# print(tup.count(2))

# PRACTICE
# WAP to ask the user to enter names of their 3 favourite movies & store them in a list
# movies=[]
# mov1=input("enter 1st movie: ")
# mov2=input("enter 2nd movie: ")
# mov3= input("enter 3rd movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)
# 
# movies=[]
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2nd movie: "))
# movies.append(input("enter 3rd movie: "))
# print(movies)


# WAP to check if a list contains a palindrome of elements(Hint:use copy() method)
# list1=[1,2,1]
# list2=[1,2,3];
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")
    
    
#  WAP to count the number of students with the "A" grade in the following tuple
# grade=("C","D","A","B","B","A")
 
# print(grade.count("A"))


# WAP to store the above values in list & sort them from "A" to "D"

grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)







