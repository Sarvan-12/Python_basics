"""
wap to enter marks of 3 subjects from the user and store them in a dic.
start with an empty dic and add one by one .
use sub name as key and marks as value
"""

marks={}
x=int(input("enter math marks :"))
marks.update({"math":x})
y=int(input("enter phy marks :"))
marks.update({"phy":y})
z=int(input("enter chem marks :"))
marks.update({"chem":z})
'''
x=int(input("enter math marks :"))
y=int(input("enter phy marks :"))
z=int(input("enter chem marks :"))      
marks["phy":y]                           #error
marks["chem":z]
marks["math":x]
'''
print(marks)