# Creating a School library program using the Library class and the UserInterface class.

import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.font
import tkinter.ttk
import tkinter.scrolledtext
import tkinter.dnd
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog


class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + " Year: " + self.year + " ISBN: " + self.isbn


class Library:
    def __init__(self):
        self.books = {}

    def addBook(self, book):
        self.books[book.isbn] = book

    def removeBook(self, isbn):
        del self.books[isbn]

    def findBook(self, isbn):
        return self.books[isbn]

    def __str__(self):
        return str(self.books)


class UserInterface:
    def __init__(self, library):
        self.library = library
        self.window = tkinter.Tk()
        self.window.title("Library")
        self.window.geometry("300x200")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self.titleFrame = tkinter.Frame(self.window)
        self.titleFrame.pack()
        self.titleLabel = tkinter.Label(self.titleFrame, text="Title")
        self.titleLabel.pack(side="left")
        self.titleEntry = tkinter.Entry(self.titleFrame)
        self.titleEntry.pack(side="left")
        self.authorFrame = tkinter.Frame(self.window)
        self.authorFrame.pack()
        self.authorLabel = tkinter.Label(self.authorFrame, text="Author")
        self.authorLabel.pack(side="left")
        self.authorEntry = tkinter.Entry(self.authorFrame)
        self.authorEntry.pack(side="left")
        self.yearFrame = tkinter.Frame(self.window)
        self.yearFrame.pack()
        self.yearLabel = tkinter.Label(self.yearFrame, text="Year")
        self.yearLabel.pack(side="left")
        self.yearEntry = tkinter.Entry(self.yearFrame)
        self.yearEntry.pack(side="left")
        self.isbnFrame = tkinter.Frame(self.window)
        self.isbnFrame.pack()
        self.isbnLabel = tkinter.Label(self.isbnFrame, text="ISBN")
        self.isbnLabel.pack(side="left")
        self.isbnEntry = tkinter.Entry(self.isbnFrame)
        self.isbnEntry.pack(side="left")
        self.buttonFrame = tkinter.Frame(self.window)
        self.buttonFrame.pack()
        self.addButton = tkinter.Button(self.buttonFrame, text="Add", command=self.add)
        self.addButton.pack(side="left")
        self.removeButton = tkinter.Button(self.buttonFrame, text="Remove", command=self.remove)
        self.removeButton.pack(side="left")
        self.findButton = tkinter.Button(self.buttonFrame, text="Find", command=self.find)
        self.findButton.pack(side="left")
        self.quitButton = tkinter.Button(self.buttonFrame, text="Quit", command=self.quit)
        self.quitButton.pack(side="left")

    def run(self):
        self.window.mainloop()

    def add(self):
        title = self.titleEntry.get()
        author = self.authorEntry.get()
        year = self.yearEntry.get()
        isbn = self.isbnEntry.get()
        book = Book(title, author, year, isbn)
        self.library.addBook(book)
        tkinter.messagebox.showinfo("Add", "Book added")

    def remove(self):
        isbn = self.isbnEntry.get()
        self.library.removeBook(isbn)
        tkinter.messagebox.showinfo("Remove", "Book removed")

    def find(self):
        isbn = self.isbnEntry.get()
        book = self.library.findBook(isbn)
        tkinter.messagebox.showinfo("Find", book)

    def quit(self):
        self.window.destroy()
        self.window.quit()


def main():
    library = Library()
    ui = UserInterface(library)
    ui.run()


main()
