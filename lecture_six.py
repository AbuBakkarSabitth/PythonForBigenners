# def cum(a,b):
#     # a=1
#     # b=10
#     sum=a+b
#     return sum
# r= cum(2,10)
# print(r)
#function definition
# def calc_sum(a,b):
#     return a+b
# sum =  calc_sum(1,2) #function call;arguments
# print(sum)

# def print_hello():
#     print("hello")
# print_hello()
# output=print_hello()
# print(output) #output none.BCZ this function didn't return anything
# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# avgs=calc_avg(98,97,95)
# print(avgs)

#Funtion 2 types: Built in function,User-defined functions
#DEFAULT Parameters
#Assigning a default value to parameter,which is used when no argument is passed

# def cal_prod(a=2,b=3): #We should not write cal_prod(a=3,b)
#         print(a*b)
#     return a*b;

# d=cal_prod()
# print(d)

#WAF to print the length of a list(list  is the parameter)
# cities=["delhi","gurgaon","noida","pune","mumbai"]
# heroes=["thor","ironman","captin america","shaktiman"]
# def print_len(list):
#     print(len(list))

#WAF to print the elements of a list in a single line(list is the parameter)
# def print_len(list):
#     for item in list:
#         print(item, end=" ")
#         # print(item, end="\n")

# print_len(cities)

#WAP to find the factorial of n(n is the parameter)

# n=5
# for i in range(i,n+1):fact=1

#     fact *=i
# print(fact)
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# cal_fact(5)    

# #WAF to cnvert USD TO INR
# def converter(usd_val):
#    inr_val= usd_val *83
#    print(usd_val,"USD =",inr_val,"INR")

# converter(78)


#RECURSION,When a function calls itself repeatedly
# def show(n):
#     if(n==0):
#         return
#     print(n)
# #recursive function
# def show(n):
#     a=123
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END",n)
# show(3)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(4))

    
  

#Write a recursive function to calculate the sum of first n natural numbers

# def calc_sum(n):
#     if(n==0):
#         return  0
#     print(n)
#     return calc_sum(n-1) +n
# sum=calc_sum(10)
# print(sum)


#Write a recursive  function to print all elements in a list.
#Hint: use list & index as parameters
fruits= ["mango","litchi","apple","banana"]
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx],end="\n")
    print_list(list,idx+1)
fruits=["mango","litch","apple","banana"]
print_list(fruits,0)