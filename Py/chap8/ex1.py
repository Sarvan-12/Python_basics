f = open(r"C:\Users\sarvan\Desktop\Py\chap8\demo.txt", "r")   #read
data = f.read()
#words=f.read(5)    reads only 5 char
#line1=f.readline()    #reads 1 line
#line2=f.readline()
print(data)
#print(words)
#print(line1)
#print(line2)
print(type(data))
f.close()

#'r'=open for reading(default)
#'w'=open for writing,overwrite 
#'x'=create a new file and open it for writing
#'a'=open for writng,appending to the end of the file if it exits
#'b'=binary mode
#'t'=text mode(default)
#'+'=open a disk file for updating(read and write)