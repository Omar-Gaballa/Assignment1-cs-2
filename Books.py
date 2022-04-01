class Books:
    # book_List = []

    def __init__(self, title, authors, isbn, tc, On_Phy):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.copies_Borrowed = 0
        self.total_copies = tc
        self.available = self.total_copies - self.copies_Borrowed
        self.online_Physical = On_Phy
        self.loan_Period = 10
        self.borrowed_By = []
        # self.book_List.append(self)

    def set_borrwer_Info(self, boo, use):
        if boo:
            self.borrowed_By.append(use)
        elif not boo:
            for i in range(len(self.borrowed_By)):
                if self.borrowed_By[i] == use:
                    self.borrowed_By.pop(i)
        else:
            raise TypeError

    def set_loanperiod(self, extention):
        self.loan_Period += extention

    def set_borrowed(self, boo):
        if boo:
            self.copies_Borrowed += 1
        elif not boo:
            self.copies_Borrowed -= 1
        else:
            raise TypeError

    def get_title(self):
        return self.title

    '''def __eq__(self, other):
        return self.title == other.title'''
