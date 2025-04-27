#recursion
def show(n):
    if n==0:    #base case
        return 
    print(n)
    show(n-1)
    print("END")    #callstack

show(5)     #5,4,3,2,1