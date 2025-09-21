def avg_marks():
    av={}
    for i in students.keys():
        tot=sum(students[i])
        avg=tot/len(students[i])
        av[i]=avg
    print("Average Marks:",av)
    m=max(av,key=av.get)
    print("Top Performer : ",m)
        
students={}
n=int(input("Enter no of Students : "))
print("Student Details")
for i in range(n):
    n=input("Enter Student name : ")
    m=list(map(int,input("Enter marks : ").split()))
    students[n]=m
print("Students : ",students)
avg_marks()