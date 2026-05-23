"""
u r gn a list of subjects .Assume 1 classroom is req for 1 sub.
how many classrooms r needed by all students
'python','java','c++','python','js','java','python','java','c++','c'
"""
set1={'python','java','c++','python','js','java','python','java','c++','c'}
print(set1)
print(len(set1))

for x in set1:
    print(x)
    
print('python' not in set1)

set1.add("DSA")
print(set1)

set2 = { "apple", "samsung"}
set1.update(set2)
print(set1)

list1 = ["asd","shd","sga"]
set1.update(list1)
print(set1)

set1.remove("asd")
set1.remove("shd")
set1.remove("sga")
print(set1)

# set1.remove("adc")  this will cause error
set1.discard("adc")
print(set1)

set1.pop()
print(set1)

set2.clear()
print(set2)

del set2
# print(set2)   this will cause error
