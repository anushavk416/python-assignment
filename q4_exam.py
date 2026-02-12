class Exam:
    pass_marks = 40
    
    def __init__(self, sname, subname, total_marks):
        self.sname = sname
        self.subname = subname
        self.total_marks = total_marks
        self.submitted = False
        self.score = 0
    
    def start_exam(self):
        print("exam started.")

    def submit_exam(self, score):
        self.submitted = True
        self.score = score

    def calculate_score(self):
        if self.submitted:
            if self.score < Exam.pass_marks:
                print("Fail.")
            return self.score
        else:
            print("exam not submitted.")
            return 0

    @classmethod
    def update_pass_marks(cls, new_pass):
        cls.pass_marks = new_pass

e1 = Exam("anusha", "MATH", 100)
e1.start_exam()
e1.submit_exam(78)
print("Score:", e1.calculate_score())
print("Pass Marks:", Exam.pass_marks)

Exam.update_pass_marks(45)
print("Updated Pass Marks:", Exam.pass_marks)

e2 = Exam("savitri", "DSP", 100)
e2.start_exam()
e2.submit_exam(45)
print("Score:", e2.calculate_score())
