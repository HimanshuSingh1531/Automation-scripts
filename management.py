# Library Management System in Python

class Book:
    def __init__(self, title, author, isbn, copies):
        """Constructor for Book class"""
        self._title = title          # Encapsulated attributes (private)
        self._author = author
        self._isbn = isbn
        self._copies = copies

    # Getter for title (encapsulation)
    def get_title(self):
        return self._title

    # Getter for author
    def get_author(self):
        return self._author

    # Getter for ISBN
    def get_isbn(self):
        return self._isbn

    # Getter for available copies
    def get_copies(self):
        return self._copies

    # Method to borrow a book
    def borrow_book(self):
        if self._copies > 0:
            self._copies -= 1
            print(f"Book '{self._title}' borrowed successfully.")
        else:
            print(f"Sorry, '{self._title}' is currently unavailable.")

    # Method to return a book
    def return_book(self):
        self._copies += 1
        print(f"Book '{self._title}' returned successfully.")

    def __str__(self):
        """String representation of a book"""
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Available Copies: {self._copies}"


class Member:
    def __init__(self, name, member_id):
        """Constructor for Member class"""
        self._name = name             # Encapsulated attributes
        self._member_id = member_id
        self._borrowed_books = []     # List of borrowed books

    def borrow(self, book):
        """Method for borrowing a book"""
        if len(self._borrowed_books) >= 3:
            print(f"{self._name} cannot borrow more than 3 books.")
        else:
            book.borrow_book()
            self._borrowed_books.append(book)

    def return_book(self, book):
        """Method for returning a book"""
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
        else:
            print(f"{self._name} does not have '{book.get_title()}' borrowed.")

    def __str__(self):
        """String representation of a member"""
        borrowed_titles = [book.get_title() for book in self._borrowed_books]
        return f"Member: {self._name}, ID: {self._member_id}, Borrowed Books: {', '.join(borrowed_titles)}"


class Library:
    def __init__(self, name):
        """Constructor for Library class"""
        self._name = name             # Encapsulated attributes
        self._books = {}              # Dictionary to store books using ISBN as key

    def add_book(self, book):
        """Method to add a book to the library"""
        if book.get_isbn() in self._books:
            print(f"Book '{book.get_title()}' already exists in the library.")
        else:
            self._books[book.get_isbn()] = book
            print(f"Book '{book.get_title()}' added to the library.")

    def remove_book(self, isbn):
        """Method to remove a book from the library"""
        if isbn in self._books:
            removed_book = self._books.pop(isbn)
            print(f"Book '{removed_book.get_title()}' removed from the library.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def search_by_title(self, title):
        """Search for a book by title"""
        for book in self._books.values():
            if book.get_title().lower() == title.lower():
                print(book)
                return book
        print(f"No book found with title '{title}'.")
        return None

    def display_books(self):
        """Method to display all available books"""
        if self._books:
            print(f"Books available in {self._name}:")
            for book in self._books.values():
                print(book)
        else:
            print(f"No books available in {self._name}.")

# Main function to demonstrate the Library Management System
def main():
    library = Library("City Central Library")
    
    # Creating Book objects
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3)
    book2 = Book("1984", "George Orwell", "9780451524935", 2)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467", 4)
    
    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Displaying available books
    library.display_books()
    
    # Creating Member objects
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    
    # Members borrow books
    member1.borrow(book1)
    member1.borrow(book2)
    member2.borrow(book3)
    
    # Displaying borrowed books for each member
    print(member1)
    print(member2)
    
    # Members return books
    member1.return_book(book1)
    member2.return_book(book3)
    
    # Display the updated library after transactions
    library.display_books()

# Running the main function
if __name__ == "__main__":
    main()
