def check_item(t):
    for i in menu:
        if i==t:
            return True
    return False
def add_item(it):
    if check_item(it)==True:
        print(it," is already Available in the Menu.")
    else:
        menu.append(it)
        print(it,"is added to the Menu.")
def remove_item(t):
    
    if check_item(t)==True:
        menu.remove(t)
        print(t," is removed from the Menu.")
    else:
        print(t,"is not Available in the Menu.")   
menu=[]
while True:
    print("1.Add item")
    print("2.Remove item")
    print("3.Check item")
    print("4.Exit")
    c=int(input("Enter your choice : "))
    if c==1:
        print("Menu :",menu)
        it=input("Enter item name : ")
        add_item(it)
    elif c==2:
        print("Menu :",menu)
        it=input("Enter item name : ")
        remove_item(it)
    elif c==3:
        it=input("Enter item name : ")
        if check_item(it)==True:
            print(it," is Available.")
        else:
            print(it," is not Available.")
    elif c==4:
        break
    else:
        print("Invalid input!Enter between 1 to 4")
    
