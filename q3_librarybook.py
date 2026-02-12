class LibraryBook:
    libName = 'Coforge'
    addr = 'kondapur'
    pin = 500084
    books = 5000
    fine_per_day = 2
    issue_duration = 14
    
    def __init__(self, bid, title):
        self.bid = bid
        self.title = title
        self.book_in = True
        self.taken_duration = 0
    
    def issue_book(self):
        if self.book_in:
            self.book_in = False #book_out
        else: print("book already issued.")
    
    def return_book(self):
        if not self.book_in:
            self.book_in = True
        else: print("book not issued.")
    
    def calculate_fine(self):
        return (self.taken_duration - LibraryBook.issue_duration)*LibraryBook.fine_per_day
    
    @classmethod
    def update_fine_per_day(cls, newfine):
        cls.fine_per_day = newfine
        
    
b1 = LibraryBook(101, "Python Programming")
b1.issue_book()

b1.taken_duration = 20
print("Fine:", b1.calculate_fine())

b1.return_book()
LibraryBook.update_fine_per_day(5)

b2 = LibraryBook(102, "Data Structures")
b2.issue_book()
b2.taken_duration = 18
print("Fine:", b2.calculate_fine())
