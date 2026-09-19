class Book:
    """Book class jo har kitab ki detail hold karti hai."""
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.book_id}] '{self.title}' by {self.author} ({status})"


class Person:
    """Base class for Inheritance."""
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def get_details(self):
        return f"ID: {self.person_id}, Name: {self.name}"


class Member(Person):
    """Member class jo Person se inherit karti hai (Inheritance & Polymorphism)."""
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.borrowed_books = []

    # Polymorphism: Base class ke method ko override kar rahe hain
    def get_details(self):
        return f"Member - {super().get_details()} | Books Borrowed: {len(self.borrowed_books)}"


class Library:
    """Main Library class jo Encapsulation and Abstraction demonstrate karti hai."""
    def __init__(self, name):
        self.name = name
        self.__books = {}    # Private attribute (Encapsulation)
        self.__members = {}  # Private attribute

    def add_book(self, book):
        self.__books[book.book_id] = book
        print(f"Book '{book.title}' library me add ho gayi.")

    def register_member(self, member):
        self.__members[member.person_id] = member
        print(f"Member '{member.name}' register ho gaye.")

    def issue_book(self, book_id, member_id):
        if book_id not in self.__books:
            print("Galti: Kitab nahi mili!")
            return
        if member_id not in self.__members:
            print("Galti: Member register nahi hai!")
            return

        book = self.__books[book_id]
        member = self.__members[member_id]

        if not book.is_available:
            print(f"Sorry, '{book.title}' abhi available nahi hai.")
        else:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"Success: '{book.title}' issue ho gayi {member.name} ko.")

    def return_book(self, book_id, member_id):
        if book_id in self.__books and member_id in self.__members:
            book = self.__books[book_id]
            member = self.__members[member_id]

            if book in member.borrowed_books:
                book.is_available = True
                member.borrowed_books.remove(book)
                print(f"Success: '{book.title}' return ho gayi.")
            else:
                print("Yeh kitab is member ke paas nahi thi.")

    def display_books(self):
        print(f"\n--- {self.name} Available Books ---")
        for book in self.__books.values():
            print(book)
        print("-------------------------------\n")


# ==========================================
# Execution / Testing
# ==========================================
if __name__ == "__main__":
    # Library ka instance banana
    my_library = Library("Central City Library")

    # Books create aur add karna
    b1 = Book(101, "Python Crash Course", "Eric Matthes")
    b2 = Book(102, "Clean Code", "Robert C. Martin")
    
    my_library.add_book(b1)
    my_library.add_book(b2)

    # Members register karna
    m1 = Member(1, "Rahul Sharma")
    my_library.register_member(m1)

    # Available Books dekhna
    my_library.display_books()

    # Book Issue karna
    my_library.issue_book(101, 1)

    # Double issue check karna
    my_library.issue_book(101, 1)

    # Member details check karna (Polymorphism)
    print("\n" + m1.get_details())

    # Book Return karna
    my_library.return_book(101, 1)

    # Updated Status dekhna
    my_library.display_books()