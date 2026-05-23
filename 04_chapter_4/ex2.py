#nested dic
student={
    "name":"sarvan",
    "subjects":{
        "phy":81,
        "chem":80,
        "math":100
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["math"])

#dic methods
print(student.keys())    #returns all keys
print(list(student.keys()))   #returns all keys in lists
print(len(student))   #len of dic
print(student.values())    #returns all values
print(tuple(student.values()))    #returns all values in tuples
print(student.items())    #returns all key value pairs as tuples
print(student.get("name"))    #returns the key according to value ,if the key doesn't exist then it will return None
print(student["name"])    #same as above but this will cause error if the key does not exist in the dic
student.update({"name":"Sharvan","age":21})   #updates and adds new key values pairs
print(student)

# stu = student.copy()
stu = dict(student)



