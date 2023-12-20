class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailability: {'Available' if self.availability_status else 'Not Available'}\n")

    def update_availability(self, status):
        self.availability_status = status


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nBooks Borrowed: {', '.join(self.books_borrowed)}\n")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book.title)
            book.update_availability(False)
            print(f"{self.name} has successfully borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_availability(True)
            print(f"{self.name} has successfully returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title} from the library.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book):
        user.borrow_book(book)
        self.transactions.append(f"{user.name} borrowed {book.title}")

    def return_book(self, user, book):
        user.return_book(book)
        self.transactions.append(f"{user.name} returned {book.title}")

    def display_books(self):
        print("Library Catalog:")
        for book in self.books:
            book.display_details()

    def display_users(self):
        print("Registered Users:")
        for user in self.users:
            user.display_details()

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


def input_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    return Book(title, author, isbn)


def input_user():
    user_id = input("Enter the user ID: ")
    name = input("Enter the name of the user: ")
    return User(user_id, name)


if __name__ == "__main__":
    library_system = Library()

    while True:
        print("\n*********************************************************")
        print("***********| Library Management System |*****************")
        print("*********************************************************")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow and Return Books")
        print("4. Display Books")
        print("5. Display Users")
        print("6. Display Transactions")
        print("7. Quit")
        print("*********************************************************")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            library_system.add_book(input_book())
        elif choice == "2":
            library_system.register_user(input_user())
        elif choice == "3":
            for user in library_system.users:
                for book in library_system.books:
                    library_system.borrow_book(user, book)
                    library_system.return_book(user, book)
        elif choice == "4":
            library_system.display_books()
        elif choice == "5":
            library_system.display_users()
        elif choice == "6":
            library_system.display_transactions()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
