import logging
logging.basicConfig(
    filename = "employee.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:
    hra_percentage = 50
    company = "Google"
    incometax = 10

    def __init__(self, emp_id, name, ctc):
        self.emp_id = emp_id
        self.name = name
        self.ctc = ctc
        self.leave_days = 0
        self.deduction = 0

    def calculate_salary(self):
        tax = Employee.incometax * self.ctc / 100
        net = self.ctc - tax - self.deduction
        return net

    def apply_leave_deduction(self, leaves):
        self.leave_days += leaves
        if(self.leave_days > 10):
            self.deduction = leaves * 500
            logging.info("final deduction of salary by amount: %s",self.deduction)
        return self.deduction

    def display_payslip(self):
        logging.info("Employee: %s", self.name)
        logging.info("Salary: %s", self.calculate_salary())

    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra
        logging.info("new HRA: %s", cls.hra_percentage)
    
emp1 = Employee(1234, "Anusha", 35_00_000)
emp1.apply_leave_deduction(11)
logging.info("Salary: %s",emp1.calculate_salary())
emp1.display_payslip()
Employee.update_hra_percentage(30)


