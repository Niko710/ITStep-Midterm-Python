import json
from pathlib import Path
from typing import Any


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
        self.title = title.title()
        self.author = author.title()
        self.publish_year = year
    
    # Clear and informative represenation of book
    def __repr__(self) -> str:
        return f"Title: {self.title} | Author: {self.author} | Year: {self.publish_year}"
        

class BookManager:
    """
    BookManager manages Book objects, adds Book to the list, lists all books and searches book by title
    """
    def __init__(self) -> None:
        self.database: Path = self._get_database()

    # Getting path to database
    @staticmethod
    def _get_database() -> Path:
        filename = Path(__file__).parent/"database.json"

        if filename.exists():
            return filename
        
        structure = {
            "books": []
        }

        with open(filename, mode="w", encoding="utf-8") as f:
            json.dump(structure, f, cls=BookEncoder)

        return filename


    # Adding book to database
    def add_book(self, book: Book) -> None:
        data = self.read_database()
        data["books"].append(book)

        with open(self.database, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, cls=BookEncoder)
            

    # Reading database and returning data
    def read_database(self):
        with open(self.database, mode="r", encoding="utf-8") as f:
            data = json.load(f, object_hook=decode_book)
        return data
    

    # Listing all books in system
    def list_books(self) -> list[Book]:
        return self.read_database()["books"]


    # Searching book by user input
    def find_book(self, search: str) -> list:
        search = search.strip().lower()
        result: list = [b for b in self.read_database()["books"] if search in b.title.lower()]
        return result


# Encoder for Book serialization
class BookEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Book):
            return {
                "title": o.title,
                "author": o.author,
                "year": o.publish_year
            }

        return super().default(o)


# Decoder for book deserialization
def decode_book(dct: dict):
    if all(k in ("title", "author", "year") for k in dct.keys()):
        return Book(**dct)
    return dct
    

def main():
    print("Welcome to book management system!")
    book_manager = BookManager()

    while True:
        action = input("Please, choose your action (add/list/find/exit): ").strip().lower()

        if action == "add":
            book_manager.add_book(Book(get_title(), get_author(), get_publish_year()))
            print("Book was added successfully!")

        elif action == "list":
            print("Listing all books:")
            for book in book_manager.list_books(): print(book)

        elif action == "find":
            title: str = input("Enter book title to search: ")
            print("Searching for your book...")
            result: list = book_manager.find_book(title)
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