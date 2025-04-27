age=int(input("enter age:"))
vote=("yes","no")[age<18]    #(false,true)[condition]
print(vote)
light=input("enter light: ")
signal=("stop","go")[light=="green"]
print(signal)