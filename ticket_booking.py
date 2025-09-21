def book_seat(t):
    if t<=n and t in aseats:
        bseats.add(t)
        aseats.remove(t)
        print("Booking confirmed. Seat No : ",t)
    else:
        print("Seat No ",t,"is not avaialable.")
def cancel_seat(t):
    if t<=n and t in bseats:
        bseats.remove(t)
        aseats.add(t)
        print("Cancellation Successfull : Seat No ",t,"is canceled.")
    else:
        print("Cancellation Failed : Seat is not booked.")
def seats():
    print("Total Seats :",n)
    print("Booked Seats : ",bseats)
    print("Available Seats : ",aseats)
      
bseats=set()
n=int(input("Enter Total Seats : "))
aseats=set(range(1,n+1))
while True:
    print("1.Book Seat")
    print("2.Cancel Seat")
    print("3.Booked and Available seats")
    print("4.Exit")
    c=int(input("Enter your choice : "))
    if c==1:
        print("Available Seats : ",aseats)
        se=int(input("Enter Seat No : "))
        book_seat(se)
    elif c==2:
        print("Booked Seats : ",bseats)
        se=int(input("Enter Seat No : "))
        cancel_seat(se)
    elif c==3:
        print("Seat Bookings : ")
        seats()
    elif c==4:
        break
    else:
        print("Invalid input!Enter between 1 to 4")
    