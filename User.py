from Books import *


class User:
    user_List = []
    bookList = []

    def __init__(self, name, iD):
        self.name = name
        self.id = iD
        self.borrowedBooks = 0
        self.Email = self.name + "@gmail.com"
        self.user_List.append(self)

    def get_credentials(self):
        return self.name, self.id

    def get_borrowedBooks(self):
        return self.borrowedBooks

    def get_id(self):
        return self.id

    def authintication(self):
        if isinstance(self, Admin):
            return "Admin"
        elif isinstance(self, Librarian):
            return "Librarian"
        elif isinstance(self, NormalUser):
            return "Normal User"

    def search(self, book_name):
        for i in self.bookList:
            if i.get_title() == book_name:
                print(i.get_title())
            else:
                print("Book not found!!")

    def show(self):
        for i in self.bookList:
            print(i.get_title())

    def get_name(self):
        return self.name

    def get_stats(self):
        op = 0
        total = 0
        for i in self.bookList:
            if i.online_Physical:
                op += 1
            total += i.copies_Borrowed
        return "online copies: ", op, "copies borrowed: ", total


class Admin(User):  # start of Admin Class

    def __init__(self, name, iD):
        super(Admin, self).__init__(name, iD)

    def show_Users(self):
        for i in self.user_List:
            print(i.get_name(), ":", i.authintication())

    def add_Users(self, username, iD):
        NormalUser(username, iD)

    def remove_Users(self, username):
        for i in self.user_List:
            if i.get_name == username:
                self.user_List.pop(i)


class Librarian(User):  # start of Librarian Class

    def __init__(self, name, iD):
        super(Librarian, self).__init__(name, iD)

    def add_Book(self, book_name, author, sn, tc, boo):
        # for i in self.bookList:
        # if i.get_title() == book_name:   ! can be duplicated : needs to be added
        t = Books(book_name, author, sn, tc, boo)
        self.bookList.append(t)

    def remove_Book(self, book_name):
        for i in self.bookList:
            if i.get_title() == book_name:
                self.bookList.pop(i)


class NormalUser(User):  # start of Normal User Class

    def __init__(self, name, iD):
        super(NormalUser, self).__init__(name, iD)

    def Borrow(self, book_name):
        for i in self.bookList:
            if i.get_title() == book_name:  # doesn't check for available copies !!
                self.borrowedBooks += 1
                i.set_borrowed(True)
                i.set_borrwer_Info(True, self)

    def return_book(self, book_name):
        for i in self.bookList:
            if i.get_title() == book_name:
                self.borrowedBooks -= 1
                i.set_borrowed(False)
                i.set_borrwer_Info(False, self)

    def extend_Loan_period(self, book_name, extention=10):
        for i in self.bookList:
            if i.get_title() == book_name:
                i.set_loanperiod(extention)


'''y = Librarian("ahmed", 2012)
y.add_Book("looking for", "unknown", 12312, 10, True)
y.add_Book("looking for alaska", "unknown", 12312, 10, True)
print(y.bookList[0].get_title())

meh = Admin("omar", 2131)

meh.show_Users()
meh.add_Users("ana", 20132)
meh.show_Users()
x = NormalUser("test", 2021)
x.Borrow("looking for alaska")
x.return_book("looking for alaska")

print(y.get_stats())
'''