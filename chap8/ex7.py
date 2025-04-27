#waf that replace all occurences of java with python in above file
with open(r"C:\Users\sarvan\Desktop\Py\chap8\practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Python","Java")
print(new_data)

with open(r"C:\Users\sarvan\Desktop\Py\chap8\practice.txt","w") as f:
    f.write(new_data)
