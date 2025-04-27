#sets
sets={1,2,3,4,"hello",4}  #ignores dublicates
print(sets)
print(type(sets))
set1={}   #empty dic
print(type(set1))
set2 = set()
print(type(set2))

#set methods
#sets are mutable
# set elements are immutable
sets.add("world")  #adds new ele 
sets.add((1,2,3))   #cannot add lists
print(sets)
print(len(sets))
sets.remove(4)   #removes ele
print(sets)
print(sets.pop())   #pops random ele

#union and intersection
set={1,3,"world","python"}
print(sets)
print(set)
print(sets.union(set))
print(sets.intersection(set))




