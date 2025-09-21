def calculate_fare(trips):
    if len(trips)==0:
        print("No Trips")
        return 0;
    else:
        basef=50
        disf=10
        tot=0
        for i in range(len(trips)):
            fare=basef+(trips[i]*disf)
            print(f"Trip {i+1} : $",fare)
            tot=tot+fare
        return tot
trips=list(map(int,input("Enter Distances(in km) for trips : ").split()))
print("Total Fare : $",calculate_fare(trips))