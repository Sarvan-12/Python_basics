#search if the word "learning" exists in the file or not
word="learning"
with open(r"C:\Users\sarvan\Desktop\Py\chap8\practice.txt","r") as f:
    data=f.read()
    if word in data:
        print("found")
    else:
        print("not found")


