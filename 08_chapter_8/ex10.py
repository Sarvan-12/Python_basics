#from a file containing nos separated by comma ,print the count of even nos 
count=0
with open(r"C:\Users\sarvan\Desktop\Py\chap8\nos.txt","r") as f:
    data=f.read()
    print(data)
    print(len(data))

    nums=data.split(",")
    for val in nums:
        if int(val)%2==0:
            count+=1

print(count)



