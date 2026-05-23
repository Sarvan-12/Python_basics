#dictionary
dic={"name":"sarvan",
     "cgpa":8.81,
     "usn":"AD043",
     "topic":("dictionary","sets"),
     "subjects":["python","java"]}
print(dic)
print(type(dic))
print(dic["name"])
dic["name"]="Sharvan"
print(dic["name"])
dic["surname"]="salian"
print(dic)

print(dic.get("cgpa","usn"))

