#search for a no x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter a no :"))
idx=0
while idx<len(num):
    if num[idx]==x:
        print("x is the position :",idx+1)
    idx+=1

