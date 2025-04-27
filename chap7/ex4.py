#warf to print all ele in the list
movies=["kaithi","vikram","leo"]
def lists(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    lists(list,idx+1)

lists(movies)
