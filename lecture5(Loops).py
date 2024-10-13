# count =1

# count =1
# while count<=5:
#     print("hello")
#     count+=1
# print(count)
# i=1
# while i<=1000000000:
#    print("hello",i)
#    i+=1




# print("loop ended")

# i=5

# while i>=1:
#     print(i)
#     i-=1

# print("Loop ended")
# while i<6:
#     print(i)
#     i-=1    

#Above 2 while loop are infinite lope

#qs1
#Print numvbers from 100 to 1
# i=1
# while i<=100:
#     print(i)
#     i+=1


#print numbers from 100 to 1

# i=100
# while i>=1:
#     print(i)
#     i-=1
 
 #print the multiplication table of a number n

# n=int(input("enter number: "))
# while i<=10:
#     print(n*i)
#     i+=1

#print the elements of  any list by lops
# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(nums):
#     print(nums[i])
#     i+=1

# heroes=["ironmen","thoe","superman","batman"]
#traverse
# idx=0
# while idx< len(heroes):
#     print(heroes[idx])
#     idx+=1    


    #Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,16,25,36,49,64,81,100,36)
x=36
i=0
# while i< len(nums):
        
#         if(nums[i]==x):
#           print("FOUND at idx", i)  
#         else:
#              print("finding")

#         i+=1  

#Break: used to terminate the loop when encounted


# while i<len(nums):
#     if(nums[i]==x):
#         print("FOUND at idx",i)
#         break;

#     else:
#         print("finding..")
#     i+=1

#Continue:terminates execution in the current iteration  & continues execution of the loop with the next iteration



# i=0
# while i<=5:
    
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=0
# while i<=10:
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#Above codes outputs all odd number
#FOR LOOPS

# veggies =["potato","brinjal","ladyfinger","cucumber"]
# for val in veggies:
#     print(val)


# tup = (1,2,3,4,2,8,9)
# for num in tup:
#     print(num)
    
# str="apnacollege"


# for char in str:
#     print(char)
# str="ApnaCollege"
# for char in str:
#     if(char=='o'):
#         print("o found")
#         break
#     print(char)

# print("END")

#Print the elements of following list using a loop:[1,4,9,16,25,36,49,64,81,100]
# list=[1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)

#Search for a number x in tuple using loop [1,4,9,16,25,36,49,64,81,100,49]
# num=(1,4,9,16,25,36,49,64,81,100,49)
# x=49
# idx=0
# for el in nums:
#     if(el==x):
#         print("number found at index",idx)
#         break
#     idx+=1


#Range functions returns a sequence  of numbers,starting from 0 by default,and increments by 1(by defaults), and stops before a specified number.
# seq= range(10)
# for i in seq:
#     print(i)
#range(start?,stop,step?) #stop is compulsary
# for i in range(10):
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(2,100,2):
#     print(i)    

#     # output:2
# 4
# 6
# 8(all are even)
#for odd number
# for i in range(1,100,2):
#     print(i)
   #using for and range() 
#print numbers from 1 to 100
# for i in range(1,101):
#     print(i)
#print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

#print the multiplication table of a number n
# n=int(input("Enter a number for multipication "))
# for i in range(1,11):
#     print(n*i)

#Pass statement
#pass is a null statement that does not do anything.It is used as a placeholder for future code.

for i in range(5):
    pass #it will skip.without pass,the code will be error

if(i>5):
    pass
print("some useful work")
#we use pass for the purpose for future plan in loops and if statement

#WAP to find the sum of first n numbers(using while)
n=7
sum=0
# for i in range(i,n+1):
#     sum+=i
# print("TOTAL SUM=",sum)
# i=1
# while i<=n:
#     sum+=i
    
#     i+=1
# print(sum)

#WAP to fund the factorial of first n numbers(using for)
# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("facrtorial =",fact)

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial =",fact)