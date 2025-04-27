#print the ele of the following list using for loop:
#[1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)

#search ele x in that
x=int(input("enter a no :"))
idx=0
for j in num:
    if j==x:
        print("x is found at index ",idx)
        break
    idx+=1