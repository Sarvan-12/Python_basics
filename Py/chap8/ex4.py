with open(r"C:\Users\sarvan\Desktop\Py\chap8\demo.txt","r") as f:
    data=f.read()
    print(data)
    #f.close() nis not req

with open(r"C:\Users\sarvan\Desktop\Py\chap8\demo.txt","w") as f:
    f.write("I'm learning python from apna clg")