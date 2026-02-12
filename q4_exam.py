class Exam:
    pass_score = 40
    
    def __init__(self, sname, subname, total_marks):
        self.sname = sname
        self.subname = subname
        self.total_marks = total_marks
        self.submitted = False
        self.marks = 0
        self.score = 0
    
    def start_exam(self):
        print("exam started.")

    def submit_exam(self, marks):
        self.submitted = True
        self.marks = marks

    def calculate_score(self):
        self.score = (self.marks/self.total_marks)*100
        if self.submitted:
            if self.score < Exam.pass_score:
                print("Fail.")
            return self.score
        else:
            print("exam not submitted.")
            return 0

    @classmethod
    def update_pass_score(cls, new_pass):
        cls.pass_score = new_pass

e1 = Exam("anusha", "MATH", 100)
e1.start_exam()
e1.submit_exam(78)
print("Score:", e1.calculate_score())
print("Pass score:", Exam.pass_score)

Exam.update_pass_score(45)
print("Updated Pass Score:", Exam.pass_score)

e2 = Exam("savitri", "DSP", 120)
e2.start_exam()
e2.submit_exam(45)
print("Score:", e2.calculate_score())
