'''waf to find in which line of the file does the word "learning"
occur 1st print -1 if not found'''
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open(r"C:\Users\sarvan\Desktop\Py\chap8\practice.txt","r") as f:
        while data:
            data=f.readline()
            if word in data:
                print(line_no)
                return
            line_no+=1
    return

check_for_line()

