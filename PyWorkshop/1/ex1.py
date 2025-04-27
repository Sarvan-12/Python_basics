# join sets

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"a",1,"d"}
set4 = {4,3,"e","a"}

# myset = set1.union(set1,set2,set3)
# or 
myset = set1 | set2 | set3
print(myset)

# set5 = set1.intersection(set3)
set5 = set1&set3 
print(set5)

# set6 = set1.difference(set3)
set6 = set1 - set3
print(set6)

# set7 = set1.symmetric_difference(set3)
set7 = set1 ^ set3
print(set7)