
def add_items():
    it=input("Enter item name : ")
    pr=eval(input("Enter Price :"))
    cart_items[it]=pr
def tot_price():
    if len(cart_items)==0:
        print("Cart is empty")
    total=sum(cart_items.values())
    print("cart : ",cart_items)
    print("Total price of items in cart = ",total)
    if len(cart_items)>5:
        dis=0.1*total
        print("Applied 10% discount = ",dis)
        print("Total Price after applying discount = ",total-dis)
      
cart_items={}
while True:
    print("1.Add item")
    print("2.Total price")
    print("3.Exit")
    c=int(input("Enter your choice : "))
    if c==1:
        add_items()
    elif c==2:
        tot_price()
    elif c==3:
        break
    else:
        print("Invalid input!Enter between 1 to 3")
