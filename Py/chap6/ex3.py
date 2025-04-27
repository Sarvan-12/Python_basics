print("sarvan",end="  ")    
print("suvarna")

def cal_prod(a=1,b=2):   
    print(a*b)
    return a*b
cal_prod()
cal_prod(3,4)


'''
def cal_prod(a,b=2):   #valid
    print(a*b)
    return a*b   
cal_prod(1)  
cal_prod(4,5)   
'''
'''
def cal_prod(a=2,b):   #not valid
    print(a*b)
    return a*b
cal_prod(1)
'''