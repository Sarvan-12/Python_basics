#waf to print the len of a string
movies=["dilli","vikram","leo"]
food=["meen","kori","yetti","marvai"]
a="Sharvan"
def print_len(list):
    print(len(list))
print_len(movies)
print_len(food)
print_len(a)


#waf to print the ele of list in a single line 

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(movies)
print()
print_list(food)



