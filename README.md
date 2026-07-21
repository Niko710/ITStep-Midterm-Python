# ITStep Python Midterm Project

This repository contains my three console projects for the ITStep Backend Python
midterm. I made them to practise working with user input, functions, files,
JSON data, and basic OOP.

## Projects

### Translator

This program translates words between Georgian and English. The user chooses the
language direction, enters a word or some words, and gets the translation. If a
word is missing, it can also be added to the dictionary.

- Georgian → English and English → Georgian modes
- Dictionary data stored in `translate/geo-eng.json` and
  `translate/eng-geo.json`
- The dictionary is updated through a temporary file

Run it with:

```bash
python3 translate/main.py
```

### ATM Simulator

This is a simple ATM simulation. A user can register, log in, check their
balance, deposit money, and withdraw money if there is enough balance.

- User records and balances stored in `atm/users.json`
- Unique numeric IDs for newly registered users
- `Decimal` is used for balance calculations
- Basic validation for usernames, passwords, and amounts

```bash
python3 atm/main.py
```

> This is only a practice project. The users in `users.json` are sample users,
> so real personal information or real passwords should not be added there.

### Book Management System

This project manages a small list of books in the console. It uses `Book` and
`BookManager` classes. Books are kept only while the program is running.

- Add books with title, author, and publication year
- List every book with clear details
- Search titles case-insensitively, including partial matches
- Validate required text fields and numeric publication years

```bash
python3 book-management-system/main.py
```

## What I Used

- Variables, conditions, loops, lists, dictionaries, and user-defined functions
- Input validation and error messages
- Reading, creating, and updating JSON files
- `pathlib` for working with file paths
- Classes, methods, and `__repr__` in the Book Management project
- Type hints and docstrings in some parts of the code

## How to Run

### Requirements

- Python **3.10** or newer
- No third-party packages — the projects use only the Python standard library

Open a terminal in the project folder and run one of the commands above. Every
project has a small menu. Type `exit` when you want to close the program.

## Repository Structure

```text
.
├── atm/
│   ├── main.py                 # ATM console application
│   └── users.json              # Sample accounts and saved balances
├── book-management-system/
│   └── main.py                 # Book and BookManager application
├── translate/
│   ├── main.py                 # Translator console application
│   ├── eng-geo.json            # English-to-Georgian dictionary
│   └── geo-eng.json            # Georgian-to-English dictionary
└── README.md
```
