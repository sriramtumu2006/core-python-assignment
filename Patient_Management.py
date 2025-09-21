class Patient:
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
def search_dis(sdis):
    l=[]
    for i in pat:
        if i.disease==sdis:
            l.append(i.name)
        print(f"Patients with {sdis} : {l}")
pat=[]
n=int(input("No of records : "))
print("<--------Patient Records--------->")
for i in range(n):
    name=input("Name : ")
    age=int(input("Age : "))
    disease=input("Disease : ")
    p=Patient(name,age,disease)
    pat.append(p)
sdis=input("Enter disease to Search for Patients : ")
search_dis(sdis)