class LibraryDatabase:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, genre, available_copies):
        self.books[book_id] = {
            'title': title,
            'author': author,
            'genre': genre,
            'available_copies': available_copies
        }

    def retrieve_book_info(self, book_id):
        book = self.books.get(book_id)
        if book:
            print("Book Information:")
            print(f"Book ID: {book_id}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Available Copies: {book['available_copies']}")
        else:
            print("Book not found in the library.")

    def update_available_copies(self, book_id, new_available_copies):
        book = self.books.get(book_id)
        if book:
            book['available_copies'] = new_available_copies
            print("Available copies updated successfully.")
        else:
            print("Book not found in the library.")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("All Books:")
        for book_id, book in self.books.items():
            print(f"Book ID: {book_id}, Title: {book['title']}")

# Creating an instance of the LibraryDatabase
library_db = LibraryDatabase()

while True:
    print("\n1. Add new book")
    print("2. Retrieve book information")
    print("3. Update available copies")
    print("4. Display information of all books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        available_copies = int(input("Enter available copies: "))
        library_db.add_book(book_id, title, author, genre, available_copies)
        print("Book added successfully.")

    elif choice == '2':
        book_id = input("Enter book ID: ")
        library_db.retrieve_book_info(book_id)

    elif choice == '3':
        book_id = input("Enter book ID: ")
        new_available_copies = int(input("Enter new available copies: "))
        library_db.update_available_copies(book_id, new_available_copies)

    elif choice == '4':
        library_db.display_all_books()

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
