#range()
seq=range(5)
print(seq)
for i in seq:
    print(i)
print("end")
for j in range(10):   #range(stop)   0-9
    print(j)
print("end")
for j in range(2,10):   #range(start,stop)    2-9
    print(j)
print("end")
for j in range(2,10,2):   #range(start,stop,step size)      2,4,6,8
    print(j)
print("end")