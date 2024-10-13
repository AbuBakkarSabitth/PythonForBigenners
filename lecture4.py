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
collection = {"hello","apnaCollege","coding","python"}


print(collection.pop())

