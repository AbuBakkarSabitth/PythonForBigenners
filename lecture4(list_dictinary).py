# info={

# "key":"value",
# "name":"apnacollege",
# "subjects" : ["python","C","Java"],
# "topics":("dict","set"),
# "learning":"coding",
# "age":35,
# "is_adult": True,
# "marks":95.5,
# 12.99:34

# }
# dictionary's element is mutable.
# print(info)
# print(type(info))

# They are unordered,mutable& don't allow duplicate keys

# print(info["name"])

# print(info["marks"])

# null_dict={}
# null_dict["name"]="apnaCollege"
# print(null_dict)


# student={


# "name" :"Abu Bakkar Sabith",
# "subjects":{
# "phy" :87,
# "chem" :45,
# "math" :6


# }

# }
# print(student)
# print(student.keys())
# print(list(student.keys()))
# # print(len(student))
# print(len(list(student.keys())))
# print(list(student.values()))
# # print(student["name"])
# print(student.get("name2"))  #no error-> return none

# if one code is error,every none error code is error


# print("hi")
# print("welcome to")
# print("apnacollege")
# print("coding")
# new_dict={"city":"delhi","age":15}
# student.update(new_dict)
# # student.update({"city":"delhi"})
# print(student)



# SET




# Set is the collection of the unordered items.Each element in the set must be unique & immutable
# We can inside boolean,int,float,str,tuple.Exception:list,dict
# collection={1,2,3,4,"hello","world",4} #don't follow order
# print(collection)
# print(type(collection)) 
# print(len(collection)) #total number of items

# collection=set() #emty set;syntax
# print(type(collection))
# collection.add(1);
# collection.add(2)
# print(collection)
# collection={1,2,2,3,4,"hello","world",4} #But only one value which has same number
# print(collection)
# print(len(collection))
#set.add(el) #adds an element
#set is mutable.But set's element is immutable


# collection = {"hello","apnaCollege","coding","python"}

# collection.add(1);
# collection.add(2);
# print(collection.pop()) #randomly pop
# print(collection) #{2, 'python', 'coding', 'apnaCollege', 'hello'}



#set.union(set2) #combines both set values &returns new
#set.intersection(set2) #combines common values & returns new

# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2)) #{1, 2, 3, 4}
# print(set1.intersection(set2)) #{2, 3}


#practice
#Store following word meanings in a python dictionary:
#table:"a piece of furniture","list of facts & figures"
#cat: "a small animal"


#ANS:
# dictionary={
#     "cat": "a small animal",
#     "table":["a piece of information","list of facts & figures"] #Can store in tuple and set

# }
# print(dictionary)


#You are given a list of subjects for students.Assume one classroom is required for 1 subjects.How many classrooms are needed by all students

"python","java","C++","python","javascript","java","python","java","C++","C"

#Ans

subjects ={
    "python","java","C++","javascript","java","python","java","C++","C"
}

print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one.Use subject name as key & marks as value
#ANS:

# marks={}
# x=int(input("enter phy: " ))

# marks.update({"phy": x})

# x=int(input("enter math: "))
# marks.update({"math" :x})
# x=int(input("enter phy: "))
# marks.update({"chem" : x})

# print(marks)


#Figure out a way to store 9 & 9.0 as separate values in a set(You can take help of built-in data types)


values={9,9.0} #it can't take same value

print(values)
values={"9",9.0}
# or,
print(values)
vales1={
    ("float",9.0),
    ("int",9)
}
print(values)
