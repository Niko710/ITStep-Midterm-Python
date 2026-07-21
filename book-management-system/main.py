# Validating title input
def get_title() -> str:
    while True:
        user_input = input("Enter book title: ").strip()
        if user_input:
            return user_input
        else:
            print("Invalid title, try again...")
    
# Validationg author input
def get_author() -> str:
    while True:
        user_input = input("Enter book author: ").strip()
        if user_input:
            return user_input
        else:
            print("Invalid author, try again...")
    
# Validationg year input
def get_publish_year() -> int:
    while True:
        user_input = input("Enter publish year: ").strip()
        if not user_input.isdecimal():
            print("Invalid date! Try again...")
            continue
        return int(user_input)
    

class Book:
    """
    Created Book object, takes 3 arguments (title, author, list)
    """
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title.capitalize()
        self.author = author.title()
        self.publish_year = year
    
    # Clear and informative represenation of book
    def __repr__(self) -> str:
        return f"Title: {self.title} | Author: {self.author} | Year: {self.publish_year}"
        

class BookManager:
    """
    BookManager manages Book objects, adds Book to the list, lists all books and searches book by title
    """
    books = []

    # Adding book to system
    @classmethod
    def add_book(cls, book: Book) -> None:
        cls.books.append(book)
    
    # Listing all books in system
    @classmethod
    def list_books(cls) -> list[Book]:
        return cls.books

    # Searching book by user input
    @classmethod
    def find_book(cls, search: str) -> list:
        search = search.strip().lower()
        result: list = [b for b in cls.books if search in b.title.lower()]
        return result
    

def main():
    print("Welcome to book management system!")

    while True:
        action = input("Please, choose your action (add/list/find/exit): ").strip().lower()

        if action == "add":
            BookManager.add_book(Book(get_title(), get_author(), get_publish_year()))
            print("Book was added successfully!")

        elif action == "list":
            print("Listing all books:")
            for book in BookManager.list_books(): print(book)

        elif action == "find":
            title: str = input("Enter book title to search: ")
            print("Searching for your book...")
            result: list = BookManager.find_book(title)
            if not result:
                print("Not found!")
            else:
                for b in result: print(b)

        elif action == "exit":
            print("Thank you for using our system! Have a nice day!")
            break

        else:
            print("Wrong command, please, try again...")


if __name__ == "__main__":
    main()