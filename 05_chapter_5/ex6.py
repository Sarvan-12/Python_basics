#break 
i=1
while i<=5:
    print(i)
    if(i==3):
        break     #returns out of while 
    i+=1
print("end of loop")

#continue
j=1
while j<=5:
    if j==3:
        j+=1
        continue   #returns to while,skips nxt lines 
    print(j)
    j+=1
