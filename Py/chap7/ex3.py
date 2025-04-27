#warf to cal sum of first n natural nos 
'''
sum=0
def sumof(n):
    if n==0:
        return 
    global sum
    sum+=n
    sumof(n-1)
    return sum
print(sumof(5))
'''
#or
def cal_sum(n):
    if n==0:
        return 0
    return n+cal_sum(n-1)
print(cal_sum(6))


