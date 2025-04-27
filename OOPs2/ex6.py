#create a class called order which stores item and its price.
#use dunder funct __gt__() to convey that :
#order1>order2 if price of order1 >2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price


ord1=Order("pen",20)
ord2=Order("scale",5)
print(ord1>ord2)    #true

