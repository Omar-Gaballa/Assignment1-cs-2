from Books import *
from User import *
import random

# ------------------------------------------
# Assignment 1
# Written by: Omar Ali Gaballa - 202101259
# ------------------------------------------
admin = Admin("Admin", 1)
librarian = Librarian("Librarian", 2)


def admin_log_in(username, password):
    for i in User.user_List:
        if i.get_name() == username and i.get_id() == password and i.authintication() == "Admin":
            # if i.authintication() == "Admin":
            print(i.get_borrowedBooks())
            print("\n"
                  "1 : to add a User to the system\n"
                  "2 : to remove a User from the system\n"
                  "3 : to show all Users currently in the system")
            u = int(input())
            if u == 1:
                l = str(input("user's name: "))
                code = int(input("user's id: "))
                i.add_Users(l, code)
            elif u == 2:
                name2 = str(input("enter the User's name "))
                i.remove_Users(name2)
                print("user has been successfully removed")
            elif u == 3:
                i.show_Users()
            else:
                print("Wrong Input")
                raise TypeError


def librarian_log_in(username, password):
    for i in User.user_List:
        if i.get_name() == username and i.get_id() == password and i.authintication() == "Librarian":
            print("1 : to add a Book to the Library\n"
                  "2 : to remove a Book from the library\n"
                  "3 : to search for a book\n"
                  "4 : to show all books currently in the Library")
            u = int(input())
            if u == 1:
                ti = str(input("Book's Title: "))
                au = str(input("Book's author: "))
                isbn = int(input("Book's serial number: "))
                tc = int(input("Book's total copies: "))
                on = bool(input("Book's availability online (True/False): "))
                i.add_Book(ti, au, isbn, tc, on)
            elif u == 2:
                name2 = str(input("enter the Book's name "))
                i.remove_Book(name2)
                print("Book has been successfully removed")
            elif u == 3:
                sear = str(input("Please enter the book's title that you wish to search for: "))
                i.search(sear)
            elif u == 4:
                i.show()
            else:
                print("Wrong Input")
                raise TypeError


def User_log_in(username, password):
    for i in User.user_List:
        if i.get_name() == username and i.get_id() == password and i.authintication() == "Normal User":
            print("1 : to borrow a Book\n"
                  "2 : to return a Book\n"
                  "3 : to search for a book\n"
                  "4 : to extend loan period")
            u = int(input())
            if u == 1:
                ti = str(input("Book's Title: "))

                i.Borrow(ti)
            elif u == 2:
                name2 = str(input("enter the Book's name "))
                i.return_book(name2)
                print("Book has been successfully returned")
            elif u == 3:
                sear = str(input("Please enter the book's title that you wish to search for: "))
                i.search(sear)
            elif u == 4:
                name = str(input("book name: "))
                i.extend_Loan_period(name)
            else:
                print("Wrong Input")
                raise TypeError

while True:
    print("Welcome to UofCanada's Library ")

    m = input("1 : Log in \n"
              "2 : Create new user")

    if m == "1":
        x = input("\n"
                  "1 : admin Log in\n"
                  "2 : Librarian Log in\n"
                  "3 : Normal User Log in")
        if x == "1":
            name = str(input("please enter your username"))
            password = int(input("please enter your password"))
            admin_log_in(name,password)


        elif x == "2":
            name = str(input("please enter your username"))
            password = int(input("please enter your password"))
            librarian_log_in(name,password)


        elif x == "3":
            name = str(input("please enter your username"))
            password = int(input("please enter your password"))
            User_log_in(name,password)


    elif m == "2":
        name = str(input("please enter your name"))
        id = random.randint(100, 500)
        x = admin.add_Users(name, id)
        print(x.get_credentials())

    en = str(input("y : to repeat\n"
                   "n : to end"))
    if en == "n":
        break
