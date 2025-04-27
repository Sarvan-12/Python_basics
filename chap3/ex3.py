#list methods
list=[2,1,3]
list.append(4)   #adds one ele at the end
print(list)
list.sort()   #sorts in asc order
print(list)
list.sort(reverse=True)   #sorts in des order 
print(list)
list.reverse()    #reverse the lists
print(list)
list.insert(1,5)   #insert ele at index
print(list)
list.remove(1)    #removes 1st occurence of the ele
print(list)
list.pop(2)  #removes ele at index
print(list)
a=[]
a.append(list[0])
a.append(list[1])
a.append(list[2])
print(a)