def positive_feedback(rating):
    if len(rating)==0:
        print("No Ratings")
        return 0
    else:
        pr=[4,5]
        co=0
        for i in rating:
            if i not in range(1,6):
                print("Rating should be between 1-5")
                return 0
        for i in rating:
            if i in pr:
                co+=1
            pos=(co/len(rating))*100 
        return pos   
rating=list(map(int,input("Enter ratings : ").split()))
pf=positive_feedback(rating)
print("Positive Feedback(4 or 5) : ",round(pf,2))