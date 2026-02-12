class Patient:
    consultfee = 300
    def __init__(self, pid, name, age, casecost):
        self.pid = pid
        self.name = name
        self.age = age
        self.adm = False
        self.casecost = casecost
        self.bill = Patient.consultfee
    
    def admit(self):
        if not self.adm:
            self.adm = True
        else: print("Patient already admitted.")
    
    def discharge(self):
        if self.adm:
            self.adm = False
        else: print("Patient isn't admitted.")
    
    def calculatebill(self):
        self.bill += self.casecost
    
    @classmethod
    def newconsultationfee(cls, newfee):
        cls.consultfee = newfee
        
p1 = Patient(101, "Anusha", 20, 2000)
p2 = Patient(102, "Rahul", 35, 1500)
p1.admit()
p1.calculatebill()
print(p1.name, "Total Bill =", p1.bill)
p1.discharge()
Patient.newconsultationfee(500)