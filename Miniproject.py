"""python Mini Project #1 | Python Tutorials For Absolute Beginners In Hindi #71
As we have nearly completed our Python object-oriented programming concepts, now it is time to do a mini-project.

Statement:-
The task is to create an “Online Library Management System”. For this, you have to create a library class that includes the following methods:

Displaybook() : To display the available books
Lendbook(): To lend a book to a user
Addbook(): To add a book to the library
Returnbook(): To return the book to the library.
As you have created a library class, now you will create an object and pass the following parameters in the constructor.

HarryLibrary=Library(listofbooks, library_name)

After that, create a main function and run an infinite while loop that asks the users for their input that whether they want to display, lend, add or return a book.



Optional:-
Maintain a dictionary for the users who own a book. Dictionary should take book name as a key and name of the person as a value. Whenever you lend a book to a user, you should maintain a dictionary.

Code as described/written in the video


# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


"""
class Library:
    def __init__(self, list_of_books, name_of_library):
        self. list_of_books=list_of_books
        self. name_of_library= name_of_library
        self.lended_book=[]

    def displaybook(self):

        for items in self.list_of_books:
             print(items)
        return f"this books available in library "

    def add_book(self, new_book):
       self.list_of_books.append(new_book.capitalize())

    def lend_book(self, books):
        if books in self.list_of_books:
            self.lended_book.append(books)
            self.list_of_books.remove(books)
            print("Book lending permission approved...")
        elif book in self.lended_book:
            print("Sorry the book is already been lended\n"
                  "Currently we only have these:- ")
            for items in self.list_of_books:
                print(items)
        else:
            print("Book's name entered is not available or name is wrong "
                  "and the available books are:- ")
            for items in self.list_of_books:
                print(items)

    def returnbook(self):
        pass


def system():
    try:
        value=True

        gnlin = Library(["marry2","kharibis","pavelretur","mazprem"],"gnlib")
        #print(gnlin.displaybook())

        while value == True:
            username = input("enter Your name")

            userInput = eval(input(f"Welcome {username} to {gnlin.name_of_library} Enter following number\n"
                                   f"1:display books\n"
                                   f"2:add books\n"
                                   f"3:Lend books\n"
                                   f"4:return book\n"
                                   f"5:exit:\n"))
            if userInput == 1:
                print(gnlin.displaybook())

            elif userInput == 2:
                new_book = input("Enter name of book you want to donate:- ")
                gnlin.add_book(new_book.capitalize())
                print("Book has been added thank you for your donation")
            elif userInput == 3:

                books = input("Enter the name of book you want to lend:- ")
                gnlin.lend_book(books.capitalize())

            else:
                print("you enter wrong keyword")
    except :
        print("error..")
        system()
system()