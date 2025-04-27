#polymorphism,when the same operator is allowed to have diff meaning according to the context

#operator overloading
print(1+2)   #add
print("sarvan "+"suvarna")    #concatinate
print([1,2,3],[4,5,6])      #merge

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def show(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):   #dunder function(2ble underscore )
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):   
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
    
num1=Complex(1,3)
num1.show()
num2=Complex(3,6)
num2.show()
num3=num1+num2
num3.show()
num4=num2-num1
num4.show()




